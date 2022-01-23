import base64
from IPython.core.display import HTML

def download(df, title=None):
    '''
    Creates an html link to download the file to local machine
    :param df: Pandas Dataframe to be downloaded
    :param title: name of the csv
    :return: download link
    '''
    csv = df.to_csv(encoding = 'utf-8')
    b64 = base64.b64encode(csv.encode(encoding='ascii',errors='replace'))
    payload = b64.decode()
    html = '<a download="{filename}" href="data:text/csv;base64,{payload}" target="_blank">{title}</a>'
    html = html.format(payload=payload,title=title,filename=title)
    return display(HTML(html))