from couchpotato.core.helpers.encoding import tryUrlencode
from couchpotato.core.helpers.variable import tryInt, getImdb
from couchpotato.core.logger import CPLog
from couchpotato.core.media._base.providers.torrent.base import TorrentProvider
from couchpotato.core.media.movie.providers.base import MovieProvider
from bs4 import BeautifulSoup
import urllib2

import traceback

log = CPLog(__name__)

class ExtraTorrent(TorrentProvider, MovieProvider):

    urls = {
        'test': 'http://extratorrent.cc/',
        'login': '',
        'login_check': '',
        'detail': 'http://extratorrent.cc/torrent/%s',
        'search': 'http://extratorrent.cc/search/?new=1&search=%s&s_cat=4',
#        'download': 'http://extratorrent.cc/download%s',
        'download': 'http://torrage.top/torrent/%s.torrent',
    }
	
    cat_ids = [(['720p'], ['720p']),(['1080p'], ['1080p']),(['brrip'], ['brrip']),(['dvdrip'], ['dvdrip']),]

    http_time_between_calls = 2 #seconds
	
#    def search(self, movie, quality):
#
#        if not quality.get('hd', False):
#            return []
#
#        return super(ExtraTorrent, self).search(movie, quality)

    def _searchOnTitle(self, title, movie, quality, results):

        #url = self.urls['search'] % tryUrlencode('%s' % (title.replace(':', '')))
        cat_ids = self.getCatId(quality)        
        url = self.urls['search'] % tryUrlencode('%s %s %s' % (title.replace(':', ''), movie['info']['year'], cat_ids)).replace('%5B%27','').replace('%27%5D','')
        log.debug('>>>> extratorrent url %s', (url))		
        #print url

        data = self.getHTMLData(url)
        if data:
            html = BeautifulSoup(data)
            try:
                resultsTable = html.find('table', attrs = {'class' : 'tl'})
                if resultsTable is None:
                   log.debug('>>>> extratorrent NADA ENCONTRADO', (url))
                   return

                #log.debug('result table %s', (resultsTable) )
                entries = resultsTable.find_all('tr')
                #log.debug('>>> result %s', (entries))
                
                for result in entries[2:]:
                    torrent_download = result.find_all('td')[0].find('a')['href'].replace('/torrent_download', '')
                    torrent_split = result.find_all('td')[0].find('a')['href'].split('/') #algum metodo retorna nada
                    torrent_id = torrent_split[2] #algum metodo retorna nada
                    torrent_title = result.find_all('td')[0].find('a')['title'].replace('Download ', '')					
                    torrent_size = self.parseSize(result.find_all('td')[3].contents[0])
                    torrent_seeders = tryInt(result.find_all('td')[4].string)
                    torrent_leechers =  tryInt(result.find_all('td')[5].string)
                    imdb_id = getImdb(torrent_title, check_inside = True)
                    #log.debug('>>>id %s', (torrent_id))
                    #log.debug('>>>title %s', (torrent_title))
                    #log.debug('>>> size %s', (torrent_size))
                    log.debug('>>> torrent_download %s', (torrent_download))
					
					#down = self.urls['download'] % torrent_download
                    #r = urllib2.Request(down)
                    #handler = urllib2.urlopen(r)
                    #link_download_torrent = handler.headers.getheader['location']
                    #log.debug('link %s' % (link_download_torrent))
                    url_detail = self.urls['detail'] % torrent_id
                    data_detail = self.getHTMLData(url_detail)
                    if data_detail:
                        html = BeautifulSoup(data_detail)
                        hash = html.find_all('td', attrs = {'class' : 'tabledata0'})[1].contents[0]
                        log.debug('>>> torrent_hash %s', (hash))
                        

                    results.append({
                       'id': torrent_id,
                       'name': torrent_title.replace('torrent', ''),
                       'url': self.urls['download'] % hash,
                       'detail_url': self.urls['detail'] % torrent_id,
                       'size': torrent_size,
                       'seeders': torrent_seeders if torrent_seeders else 0,
                       'leechers': torrent_leechers if torrent_leechers else 0,
                       'description': imdb_id if imdb_id else '',
                    })

            except:
                log.error('Failed getting results from %s: %s', (self.getName(), traceback.format_exc()))

#    def getLoginParams(self):
#        return tryUrlencode({
#            'user': self.conf('username'),
#            'pass': self.conf('password'),
#        })
#
#    def loginSuccess(self, output):
#        return '{"kod":1,"msg":"0"}' in output.lower()
#
#    loginCheckSuccess = loginSuccess
