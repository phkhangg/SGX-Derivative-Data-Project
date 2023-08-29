# SGX-Derivative-Data-Project

=== Data Team Mini Project === 
This program is a Downloader for derivative data published on https://www.sgx.com/research-education/derivatives It is written in python and run like usual Linux commands.

================================ 
Contributors: Phú Khang (phukhang11023@gmail.com) Requires: python 3 I use WSL to connect Ubuntu 22.04.2 LTS from my Windows on this project (OPTIONAL)

========= INSTRUCTIONS ========= 
Run in python virtualenv Linux commands: ./venv/bin/python main.py -* 
-a, --automation Downloads latest(today) files daily 
-c, --config=FILE_NAME Load config from FILE_NAME, default file is default.cfg 
-h, --history=DATE Download historical files according to inputs. e.g. h=20230824 
-i, --initializing Recreate date& url indextable
-u, --update Download latest(today) available files and updates indextable
-H, --help Print help information

========== INDEXTABLE ========== 
The files could be manually downloaded on https://links.sgx.com/1.0.0/derivatives-historical/*urlID/*FILETYPE e.g. : https://links.sgx.com/1.0.0/derivatives-historical/5492/WEBPXTICK_DT.zip Date—-urlID indextable is already crawled. The earlier files are not required format

========== NOFICATION ========== 
SGX may have no files sometimes on WEEKENDS, please check date before downloading historical files. The program have update function, Please confirm before recreating indextable. Network connecting failure during the process can stop donwloading, and it will not recover. Please restart. Other download failure will be recorded, please relaunched manually.

========== FILE PATH =========== 
Logging file: ./logfile.log 
Indextable: ./indextable/indextable.txt
IndexTemp for updates: ./indextable/latestindex.txt 
Download failure records: ./indextable/recovery.txt
Default cfg: ./default.cfg 
Default downloaded files PATH: ./files/*date
