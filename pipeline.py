import logging
logging.basicConfig(level=logging.INFO)
import subprocess
#import datetime

logger = logging.getLogger(__name__)
news_sites_uids = ['eluniversal', 'elpais']

def main():
    _extract()
    _transform()
    _load()

def _extract():
    logger.info('Starting extract process')
    for news_site_uid in news_sites_uids:
        subprocess.run(['python', 'main.py', news_site_uid], cwd='./extract')
        subprocess.run(['find', '.', '-name', '{}*'.format(news_site_uid), 
                        '-exec', 'mv', '{}', '../transform/{}_.csv'.format(news_site_uid), ';'],
                       cwd='./extract')
        # Windows
        #subprocess.run(['copy', r'D:\web_scrapper_curso_data_eng\final_project_live\extract\*.csv', r'D:\web_scrapper_curso_data_eng\final_project_live\transform'], shell=True)

def _transform():
    logger.info('Starting transform process')
    #now = datetime.datetime.now().strftime('%Y_%m_%d')
    for news_site_uid in news_sites_uids:
        dirty_data_filename = '{}_.csv'.format(news_site_uid)
        clean_data_filename = 'clean_{}'.format(dirty_data_filename)
        subprocess.run(['python', 'main.py', dirty_data_filename], cwd='./transform')
        subprocess.run(['rm', dirty_data_filename], cwd='./transform')
        subprocess.run(['mv', clean_data_filename, '../load/{}.csv'.format(news_site_uid)],
                         cwd='./transform')
        # Windows
        #dirty_data_filename = '{}_{datetime}_articles.csv'.format(news_site_uid,datetime=now)
        #subprocess.run(['python', 'main.py', dirty_data_filename], cwd='./transform')
        #subprocess.run(['del', dirty_data_filename], shell=True, cwd='./transform')      
        #subprocess.run(['copy', r'D:\web_scrapper_curso_data_eng\final_project_live\transform\*.csv', r'D:\web_scrapper_curso_data_eng\final_project_live\load'], shell=True)

def _load():
    logger.info('Starting load process')
    #now = datetime.datetime.now().strftime('%Y_%m_%d')
    for news_site_uid in news_sites_uids:
        clean_data_filename = '{}.csv'.format(news_site_uid)
        subprocess.run(['python', 'main.py', clean_data_filename], cwd='./load')
        subprocess.run(['rm', clean_data_filename], cwd='./load')
        # Windows
        #clean_data_filename = 'clean_{}_{datetime}_articles.csv'.format(news_site_uid,datetime=now)
        #subprocess.run(['python', 'main.py', clean_data_filename], cwd='./load')


if __name__ == '__main__':
    main()