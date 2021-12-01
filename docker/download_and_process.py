# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 12:26:49 2021

@author: jsia1
"""
import ICA_SDK
import argparse
import re
import subprocess
import multiprocessing as mp
import os
import boto3
from glob import glob
from datetime import datetime
import logging
import sys
import urllib
from collections import namedtuple
from time import sleep
#%%
logging.basicConfig(
level=logging.INFO,
format="%(asctime)s %(processName)s %(levelname)s %(message)s",
handlers=[# logging.FileHandler("debug.log", mode='w'),
    logging.StreamHandler(sys.stdout)
])

#%%

def search_name(input_dict, target):

    for i in input_dict:
        if re.match(target, i['name']):
            found=i['name']
            logging.info(f"{i['name']} found")
            break
    else:
        raise Exception(f'{target} not found')
        
    return found

def search_id(input_dict, target):

    for i in input_dict:
        if re.match(target, i['name']):
            found=i['id']
            logging.info(f"{i['name']} found")
            break
    else:
        raise Exception(f'{target} not found')
        
    return found


def search_cid(input_dict, target):
    for i in input_dict:
        if i['name']==target:
            #cid=i['id'].replace('-','')
            cid=i['id']
            logging.info(f"{i['name']} found")
            break
    else:
        raise Exception(f'{target} name not found')
        
    return cid

def search_wid(input_dict, target):
    for i in input_dict:
        if i['name']==target:
            wid=i['id'].replace('-','')
            logging.info(f"{i['name']} found")
            break
    else:
        raise Exception(f'{target} name not found')
        
    return wid

def get_s3_client(cred):
    s3_client = boto3.client('s3',
                            aws_access_key_id=cred.access_key_id,
                            aws_secret_access_key= cred.secret_access_key,
                            aws_session_token=cred.session_token)
    return s3_client

def create_folder(folder_path, foldername, volume_name, api_client):
    
    body =  ICA_SDK.CreateFolderRequest(
        name=foldername,
        folder_path=folder_path,
        volume_name=volume_name
    ) 
    dest_fol_response = ICA_SDK.FoldersApi(api_client).create_folder(body, include='ObjectStoreAccess' )
    return dest_fol_response
#%%
def create_api_client(host, domain, x_api_key, cid=None):
    configuration = ICA_SDK.Configuration(host = host)
    api_client = ICA_SDK.ApiClient(configuration)
    
    api_instance = ICA_SDK.TokensApi(api_client)
    jwt= api_instance.create_token(domain=domain,
                                   x_api_key=x_api_key,
                                   cid=cid).access_token

    
    configuration.api_key['Authorization'] = jwt
    configuration.api_key_prefix['Authorization'] = 'Bearer'
    api_client = ICA_SDK.ApiClient(configuration)
    return api_client

def filename(s, pgid, today, ext):
    filename=f'{pgid}_{today}_{s}.{ext}'

    return filename
#%%
def download_file(i : dict):
    cmd_args=['curl','-s', i['presigned_url'], '--output', i['name']]        
    response=subprocess.run(cmd_args, capture_output =True)
    logging.info(f"Downloading {i['name']} returned with exit code {response.returncode} with stderr: {response.stderr.decode('UTF-8')}")
    
def upload_file(file_name: str, fold_api_response):
    cred=fold_api_response.object_store_access.aws_s3_temporary_upload_credentials
    object_name=os.path.basename(file_name)
    s3_client=get_s3_client(cred)
    response=s3_client.upload_file(file_name, cred.bucket_name, cred.key_prefix+object_name)
    logging.info(f"{file_name} uploaded to gds://{fold_api_response.volume_name}{fold_api_response.path}")
    return response

def run_fastqc(fastqfile):
    response=subprocess.run(['/opt/bin/FastQC/fastqc','-q','-o','fastqc', fastqfile],  capture_output =True)
    #response=subprocess.run(['fastqc','-q','-o','fastqc',fastqfile],  capture_output =True)
    logging.info(f"FastQC for {fastqfile} returned with exit code {response.returncode} with stderr: {response.stderr.decode('UTF-8')}")
    
def run_md5sum(fastqfile):
    response=subprocess.run(['md5sum',fastqfile], capture_output =True)
    logging.info(f"md5sum calculation for {fastqfile} returned with exit code {response.returncode} with stderr: {response.stderr.decode('UTF-8')}")
    
    return response

def parallel_process(i: dict, fastqfile: str, fastqc_flag: str):
    download_file(i)
    md5sum_response=run_md5sum(fastqfile)
    if fastqc_flag =='true':
        run_fastqc(fastqfile)
    
    return md5sum_response
    
#%%
def main():
        #%%
    parser=argparse.ArgumentParser(description = "Grab Run Folder and FASTQ folders, perform md5sum and Fastqc", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    	
    	# Input parameters
    	# Minimum Run ID, Project ID, ICA Config, ICA ApiKey
    
    	# parser.add_argument("--ica-path", dest="ica_path", required=False, help="ICA CLI exe path", default="~/bin/ica2")
    	#parser.add_argument("--ica-path", dest="ica_path", required=False, help="ICA CLI exe path", default="opt/bin/linux/ica")
    	# parser.add_argument("--ica-config", dest="config", required=False, help="ica config file indicating server,domain, and region", default = "~/.ica/apj-config.yaml")
    	#parser.add_argument("--ica-config", dest="config", required=False, help="ica config file indicating server,domain, and region", default = "opt/resources/apj-config.yaml")
    parser.add_argument("--project-name", dest="project_name", required=True, help="ica project name specified in sample sheet that contains FASTQ files and new output folder", default ="japaninstrumenttest")
    parser.add_argument("--run-id", dest="run_id", required=True, help="Run ID to gather")
    parser.add_argument("--api-key", dest="api_key", required=True, help="ICA API Key, surround with single quotes")
    parser.add_argument("--ica-domain", dest="ica_domain", required=False, help="ICA domain", default = "ilmn-prod-apjdev")
    parser.add_argument("--ica-server", dest="ica_server", required=False, help="ICA server", default = "https://aps2.platform.illumina.com")
    parser.add_argument("--pgid", dest="pgid", required=True, help="PG ID for output folder" )
    parser.add_argument("--workgroup", dest="workgroup", required=True, help="Workgroup in BSSH")
    parser.add_argument("--runfastqc", dest="runfastqc", required=False, help="Specify 'true' or 'false' on whether to run fastqc",  
                        default='false', choices=['true','false'])
    # parser.add_argument("--uniquetsv", dest="uniquetsv", required=False, help="Specify 'true' or 'false' on whether to include run id into tsv file names",  
    #                     default='true', choices=['true','false'])
    # args = parser.parse_args(['--project-name','japaninstrumenttest',
    #                     '--run-id','211105_M02021_0243_123456789, 211117_M02021_0245_123456789',
    #                     '--api-key','cWdeSSBqrbmS*URdS$Bt6R',
    #                     '--pgid', 'PG3004',
    # 						'--ica-server', 'https://apn1.platform.illumina.com',
    # 						'--ica-domain', 'ilmn-prod-apjdev',
    #                     '--workgroup', 'japaninstrumenttest'])
    
    args = parser.parse_args()
    args.run_id=args.run_id.split(',')
    #Remove any trailing or leading whitespaces
    for i in range(len(args.run_id)):
        args.run_id[i]=args.run_id[i].strip()
    
    today=datetime.today().strftime('%y%m%d')
    
    p=urllib.parse.urlparse(args.ica_server, 'https')
    netloc=p.netloc or p.path
    newp=urllib.parse.ParseResult(scheme='https',netloc=netloc, path='', params='', query='',fragment='')
    args.ica_server=newp.geturl()
    
    logging.debug(str(args))
    #% Add project cid to bssh volume acl so that run folder can be accessed from within project context
    #Generate api client in personal context
    api_client=create_api_client(host = args.ica_server,
                                 domain=args.ica_domain,
                                 x_api_key=args.api_key)

    projects_dict = ICA_SDK.ProjectsApi(api_client).list_projects().to_dict()['items']
    cid=search_cid(projects_dict, args.project_name) #find cid of project
    #Find bssh volume name based on workgroup name
    workgroups_dict = ICA_SDK.WorkgroupsApi(api_client).list_workgroups().to_dict()['items']
    wid=search_wid(workgroups_dict, args.workgroup)
    bsshvolume=f"bssh.{wid}"
    logging.debug(f"{bsshvolume} folder acl updated")
    
    # Get bssh volume id
    api_response = ICA_SDK.FoldersApi(api_client).list_folders(volume_name=[bsshvolume], path='/')
    if api_response.item_count ==0:
        raise Exception(f"{bsshvolume} doesn't exist")
    else:
        bsshvolume_id=api_response.items[0].id
    
    # Add project cid to bssh volume acl
    api_response = ICA_SDK.FoldersApi(api_client).get_folder(bsshvolume_id)
    
    cid_acl= 'cid:'+cid
    old_acl= api_response.acl
    if cid_acl not in old_acl:
       new_acl= api_response.acl+[cid_acl]
       ICA_SDK.FoldersApi(api_client).update_folder(bsshvolume_id, body=ICA_SDK.FolderUpdateRequest(acl=new_acl))
       logging.info(f"{bsshvolume} folder acl updated")
    else:
        logging.info(f"{bsshvolume} folder acl already contains cid")
        
    
    #%% Copy fastqs to destination folder
    #Generate api client for project context
    api_client=create_api_client(host = args.ica_server,
                              domain=args.ica_domain,
                              cid=cid,
                              x_api_key=args.api_key)
    
    #Create destination folder
    base_fol_response=create_folder(folder_path=f"/{args.pgid}/{today}_report/",
                  foldername=args.pgid,
                  volume_name=args.project_name,
                  api_client=api_client)
   
        
    #Find sample volume
    samplevolume='samples-cid.'+cid
    
    #Find full name of run folder in sample volume
    folder_dict = ICA_SDK.FoldersApi(api_client).list_folders(volume_name=[samplevolume], 
                                                                   path=["/runs/*"], 
                                                                   page_size=100, 
                                                                   recursive=False).to_dict()['items']
    Jobs=namedtuple("Jobs", "fol_id job_id")
    fastq_copy_jobs=[]
    
    for run_id in args.run_id:

        
        samplerun=search_name(folder_dict, run_id)
        
        #Get list of fastqs
        fastq_dict=ICA_SDK.FilesApi(api_client).list_files(volume_name=[samplevolume], 
                                                  path=[f'/runs/{samplerun}/*'], 
                                                  recursive=True, 
                                                  page_size=1000, 
                                                  include='PresignedUrl').to_dict()['items']
        
    
    
        
        #Copy fastqs to destination folder
        fastq_parent_folder_ids=set([i['parent_folder_id'] for i in fastq_dict])
        for folder_id in fastq_parent_folder_ids:
            copyresponse=ICA_SDK.FoldersApi(api_client).copy_folder(folder_id, 
                                                       ICA_SDK.FolderCopyRequest(target_parent_folder_id=base_fol_response.id, 
                                                                                 destination_folder_name='sequence'))
            fol_id=re.search('folder:(fol.[a-zA-Z0-9]{32})#', copyresponse.parent_folder_urn).group(1)
            job_id=copyresponse.id
            
            fastq_copy_jobs.append(Jobs(fol_id, job_id))
        logging.info(f'Fastq files copy for {run_id} initiated')
    #%% Copy run data to destination folder
    #%
    # List run folders in bssh volume
    runfolder_dict=ICA_SDK.FoldersApi(api_client).list_folders(volume_name=[bsshvolume], 
                                                path=['/Runs/*'], 
                                                recursive=False, page_size=10000).to_dict()['items']
    
    run_copy_jobs=[]
    #Copy run folder in loop
    for run_id in args.run_id:
        bclrun_name=search_name(runfolder_dict, run_id)
        actual_bclrun_name=re.match('(.{6}_[a-zA-Z0-9]+_\d+_.{9})', bclrun_name).group(1)
    
        #%
        #% Create destination folder
        run_fol_response=create_folder(folder_path=f"/{args.pgid}/{today}_report/{args.pgid}/run_data/",
                                        foldername=actual_bclrun_name,
                                        volume_name=args.project_name,
                                        api_client=api_client)
        #%
        #Get id of InterOp folder
        interop_id=ICA_SDK.FoldersApi(api_client).list_folders(volume_name=[bsshvolume],
                                                               path=['/Runs/'+bclrun_name+'/InterOp/'], 
                                                               recursive=True, page_size=10000).to_dict()['items'][0]['id']
    
        #Copy to destination
        copyresponse=ICA_SDK.FoldersApi(api_client).copy_folder(interop_id,
                                                   ICA_SDK.FolderCopyRequest(target_parent_folder_id=run_fol_response.id))
        
        fol_id=re.search('folder:(fol.[a-zA-Z0-9]{32})#', copyresponse.parent_folder_urn).group(1)
        job_id=copyresponse.id
        
        run_copy_jobs.append(Jobs(fol_id, job_id))
        
        logging.info(f'InterOp folder copy for {run_id} initiated')
        
        #% Copy individual sav files to destination
        runfiles_dict=ICA_SDK.FilesApi(api_client).list_files(volume_name=[bsshvolume], 
                                                  path=[f'/Runs/{bclrun_name}/*'], 
                                                  recursive=False, 
                                                  page_size=1000,
                                                  include='PresignedUrl').to_dict()['items']
        
        upload_count=0
        for i in runfiles_dict:
            if i['name'] in ['RunInfo.xml', 'RunParameters.xml', 'SampleSheet.csv']:
                download_file(i)
                upload_file(i['name'], run_fol_response)
                upload_count+=1
        #Close upload session
        ICA_SDK.FoldersApi(api_client).complete_folder_session(run_fol_response.id, 
                                          run_fol_response.object_store_access.session_id, 
                                          ICA_SDK.CompleteSessionRequest(upload_count))

    #%% Download fastq and process in background
    os.makedirs('fastqc', exist_ok=True)
    pool=mp.Pool(mp.cpu_count())
    
    #Write headers to files
    metafilename=filename('meta',args.pgid,today, 'tsv')
    with open(metafilename, 'wt') as fh:
        fh.write('\t'.join(['fastq_name','id','flowcell_id','lib_id','index_id','lane','strand\n']))
    
    completelistfilename=filename('complete_list',args.pgid,today, 'tsv')
    with open(completelistfilename, 'wt') as fh:
        fh.write('\t'.join(['id','sample_id','complete','folder_name\n']))
        
        
    #Download the process run id fastq in loop
    for run_id in args.run_id:
        
        bclrun_name=search_name(runfolder_dict, run_id)
        actual_bclrun_name=re.match('(.{6}_[a-zA-Z0-9]+_\d+_.{9})', bclrun_name).group(1)
        
        samplerun=search_name(folder_dict, run_id)
        
        #Get list of fastqs
        fastq_dict=ICA_SDK.FilesApi(api_client).list_files(volume_name=[samplevolume], 
                                                  path=[f'/runs/{samplerun}/*'], 
                                                  recursive=True, 
                                                  page_size=1000, 
                                                  include='PresignedUrl').to_dict()['items']
        
        job_list=[]
        for i in fastq_dict:
            if i['status'] == 'Available':
                job_list.append(pool.apply_async(parallel_process, (i, i['name'], args.runfastqc)))
            else:
                logging.warning(f"{i['name']} not downloaded. Status is {i['status']}")
        

        # Block until all async processes complete. Retrieve md5sum and write out from completed background processes
        md5sumfilename=filename('MD5',args.pgid,today, 'txt')
        with open(md5sumfilename, 'at') as fh:
            for i in range(len(job_list)):
                #fastqc_jobs[i].get()
                fh.write(job_list[i].get().stdout.decode('UTF-8'))
        
        logging.info(f"md5sum written to {md5sumfilename}")
        

        # Write meta.tsv        
        fastq_names=sorted([i['name'] for i in fastq_dict])        
        sample_id=set()
        with open(metafilename, 'at') as fh:            
            for i in fastq_names:
                mg=re.match('(.{2}-.{2}-.{4}-.{1}-.{2}-.{1})-(.{9})_(.{6}_.{4}(.{4})_.{3})_S\d+_L00(\d)_(R1|R2)',i)
                fh.write('\t'.join((i,)+mg.groups())+'\n')    
                sample_id.add(mg.group(1))

        
        # Write complete_list.tsv

        sample_id_list=sorted(list(sample_id))        
        with open(completelistfilename, 'at') as fh:            
            for i in sample_id_list:                
                fh.write('\t'.join([i, i, 'Done',f'{today}_report'])+'\n')    
        
        # Delete fastqs
        to_delete=glob("./*.fastq.gz")
        for i in to_delete:
            os.remove(i)
            logging.info(f"Deleting {i} from current working directory")

        
    pool.close()
    pool.join()
    #%% Upload text files
    #Refresh upload credentials
    base_fol_response = ICA_SDK.FoldersApi(api_client).update_folder(base_fol_response.id, 
                                                                include='ObjectStoreAccess', 
                                                                body=ICA_SDK.FolderUpdateRequest())

    
        

    upload_file(md5sumfilename, base_fol_response)
    upload_file(metafilename, base_fol_response)
    upload_file(completelistfilename, base_fol_response)
    # Close upload session
    ICA_SDK.FoldersApi(api_client).complete_folder_session(base_fol_response.id, 
                                          base_fol_response.object_store_access.session_id, 
                                          ICA_SDK.CompleteSessionRequest(1) )
                
    #%% Upload FastQC results
    #Create fastqc folder
    fastqc_fol_response=create_folder(folder_path=f"/{args.pgid}/{today}_report/{args.pgid}/",
                  foldername='FastQC',
                  volume_name=args.project_name,
                  api_client=api_client)
    
    #Upload fastq results
    filelist=glob('./fastqc/*')
    for file_name in filelist:
        upload_file(file_name, fastqc_fol_response)

    # Close upload session
    ICA_SDK.FoldersApi(api_client).complete_folder_session(fastqc_fol_response.id, 
                                          fastqc_fol_response.object_store_access.session_id, 
                                          ICA_SDK.CompleteSessionRequest(len(filelist)) )
    
    #%% Check copying have completed
    logging.info("Checking fastq files copy jobs")
    for job in fastq_copy_jobs:
        
        job_query_response = ICA_SDK.FoldersApi(api_client).get_folder_job(job.fol_id, job.job_id)
        logging.info(f"Copying for {job.fol_id},  {job.job_id} is {job_query_response.progress_status}")
        while job_query_response.progress_status!='Completed':
            logging.info("Waiting for 10 seconds")
            sleep(10)
        else:
            logging.info(f"Copying for {job.fol_id},  {job.job_id} is {job_query_response.progress_status}")
    
    logging.info("Checking run interop files copy jobs")
    
    for job in run_copy_jobs:
        
        job_query_response = ICA_SDK.FoldersApi(api_client).get_folder_job(job.fol_id, job.job_id)
        logging.info(f"Copying for {job.fol_id},  {job.job_id} is {job_query_response.progress_status}")
        while job_query_response.progress_status!='Completed':
            logging.info("Waiting for 10 seconds")
            sleep(10)
        else:
            logging.info(f"Copying for {job.fol_id},  {job.job_id} is {job_query_response.progress_status}")
            

    #%% Generate and upload report_file_list.txt
    #Get all file paths in destination folder
    allfiles_dict=ICA_SDK.FilesApi(api_client).list_files(volume_name=[args.project_name], 
                                                          path=[f"/{args.pgid}/{today}_report/*"], 
                                          recursive=True, 
                                          page_size=10000).to_dict()['items']
    #Sort and write all paths to text file
    allfiles_paths=sorted([i['path'] for i in allfiles_dict])
    with open(f'{today}_report_file_list.txt' ,'wt') as fh:
        fh.write('\n'.join(allfiles_paths))

    #Get destination folder info
    parent_fold_id = ICA_SDK.FoldersApi(api_client).list_folders(volume_name=[args.project_name], 
                                                                 path=[f"/{args.pgid}/{today}_report/"], 
                                                                 recursive=True).items[0].id
    parent_fol_response = ICA_SDK.FoldersApi(api_client).update_folder(parent_fold_id, 
                                                                include='ObjectStoreAccess', 
                                                                body=ICA_SDK.FolderUpdateRequest())
    
    #Upload text file to destination folder
    upload_file(f'{today}_report_file_list.txt', parent_fol_response)
        
    # Close upload session
    ICA_SDK.FoldersApi(api_client).complete_folder_session(parent_fol_response.id, 
                                          parent_fol_response.object_store_access.session_id, 
                                          ICA_SDK.CompleteSessionRequest(1) )
    #% Remove project cid from bssh volume acl
    #Generate api client in personal context again
    api_client=create_api_client(host = args.ica_server,
                                 domain=args.ica_domain,
                                 x_api_key=args.api_key)
    #Revert acl
    ICA_SDK.FoldersApi(api_client).update_folder(bsshvolume_id, body=ICA_SDK.FolderUpdateRequest(acl=old_acl))
    logging.info(f"{bsshvolume} folder acl reverted")

    
    logging.info("All complete!")
    
    #%% Remove fastq directory
#%%
if __name__ == "__main__":

	main()