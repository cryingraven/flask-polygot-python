from polyglot.downloader import downloader
locales=['id','en','ms','ml','es','fr','ar','zh','th','ja','ko','ru','hi','nl','de']
files=['ner2','sentiment2','embeddings2']
for locale in locales:
    for file in files:
        downloader.download(file+'.'+locale)
