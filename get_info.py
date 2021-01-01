#!/usr/bin/env python
# -*- coding: utf-8 -*-
#https://www.i18nqa.com/debug/utf8-debug.html
#https://www.browserling.com/tools/utf8-encode

import os
os.environ["PYTHONIOENCODING"] = "utf-8"

import tmdbsimple as tmdb
myKey = ''
tmdb.API_KEY = myKey
tmdb_idioma = 'pt-BR'
#---------------------------------


def serie_detail(tvg_tmdbid='', postersize='200'):
    '''
    tvg_tmdbid = Series id on TMDB website
        type = string
        ex: Game of Thrones: https://www.themoviedb.org/tv/1399-game-of-thrones?language=pt-BR
        tvg_tmdbid = '1399'

    postersize = Poster image width
        type = string
        ex: 200 , 300, 500 ...
    '''
    URLYOUTUBE = 'https://www.youtube.com/watch?v='
    URLTMDBPOSTER = 'https://image.tmdb.org/t/p/w'
    URLNOPOSTER = 'https://nocover.png'

    if tvg_tmdbid != None and str(tvg_tmdbid).strip() != '':
        originaltitle = tmdb.TV(tvg_tmdbid).info()['original_name']
        print(f'TMDB Serie ID: {tvg_tmdbid}\n'
            f'Original Title: {originaltitle}\n')

        posters = ''
        posters = tmdb.TV(tvg_tmdbid).images()['posters']
        if posters != []:
            posterpath = posters[0]['file_path']
            posterpath = posterpath.strip()
            if posterpath != '' and posterpath != 'null' and posterpath != '0':
                poster = URLTMDBPOSTER + postersize + posterpath
            else:
                poster = URLNOPOSTER
            print(f'Poster: {poster}\n')
        else:
            print(f'Poster not available on TMD\n')     


        overview = ''
        overview_mylang  = tmdb.TV(tvg_tmdbid).info(language=tmdb_idioma)['overview']
        overview_mylang = overview_mylang.strip()
        if overview_mylang != '' and overview_mylang != 'null' and overview_mylang != '0':
            overview = overview_mylang
        else:
            overview_en  = tmdb.TV(tvg_tmdbid).info()['overview']
            overview_en = overview_en.strip()
            if overview_en != '' and overview_en != 'null' and overview_en != '0':
                overview = f'Only in English - {overview_en}'
            else:
                overview = ''

        if overview != '':
            print(f'Overview: {overview}\n')
        else:
            print('Overview not available on TMD\n')


        key_trailer = ''
        lang_trailer = tmdb_idioma.upper()
        trailers_mylang = tmdb.TV(tvg_tmdbid).videos(language=tmdb_idioma)['results']
        if len(trailers_mylang) > 0:
            key_trailer = trailers_mylang[0]['key']
            key_trailer = key_trailer.strip()
        else:
            trailers_en = tmdb.TV(tvg_tmdbid).videos()['results']
            if len(trailers_en) > 0:
                key_trailer = trailers_en[0]['key']
                key_trailer = key_trailer.strip()
                lang_trailer = 'EN'

        if key_trailer != '':
            print(f'Trailer: {lang_trailer} | {URLYOUTUBE}{key_trailer}\n')
        else:
            print('Trailer not available on TMD\n')

    else:
        print('TMDB Serie ID not informed\n')

    print('==========================\n')

'''
#poster: ok, overview: pt-BR , trailer: pt-BR
serie_detail('1399')

#poster: ok, overview: English , trailer: English
serie_detail('71717')

#poster: ok, overview: pt-BR , trailer: no trailer
serie_detail('36', '500')

#poster: nothing, overview: nothing , trailer: nothing
serie_detail('62608')
'''

def movie_detail(tvg_tmdbid='', postersize='200'):
    '''
    tvg_tmdbid = Movie id on TMDB website
        type = string
        ex: Os Vingadores : https://www.themoviedb.org/movie/24428-the-avengers?language=pt-BR
        tvg_tmdbid = '24428'

    postersize = Poster image width
        type = string
        ex: 200 , 300, 500 ...
    '''
    URLYOUTUBE = 'https://www.youtube.com/watch?v='
    URLTMDBPOSTER = 'https://image.tmdb.org/t/p/w'
    URLNOPOSTER = 'https://nocover.png'

    if tvg_tmdbid != None and str(tvg_tmdbid).strip() != '':
        originaltitle = tmdb.Movies(tvg_tmdbid).info()['original_title']
        print(f'TMDB Serie ID: {tvg_tmdbid}\n'
            f'Original Title: {originaltitle}\n')

        posters = ''
        posters = tmdb.Movies(tvg_tmdbid).images()['posters']
        if posters != []:
            posterpath = posters[0]['file_path']
            posterpath = posterpath.strip()
            if posterpath != '' and posterpath != 'null' and posterpath != '0':
                poster = URLTMDBPOSTER + postersize + posterpath
            else:
                poster = URLNOPOSTER
            print(f'Poster: {poster}\n')
        else:
            print(f'Poster not available on TMD\n')     


        overview = ''
        overview_mylang  = tmdb.Movies(tvg_tmdbid).info(language=tmdb_idioma)['overview']
        overview_mylang = overview_mylang.strip()
        if overview_mylang != '' and overview_mylang != 'null' and overview_mylang != '0':
            overview = overview_mylang
        else:
            overview_en  = tmdb.Movies(tvg_tmdbid).info()['overview']
            overview_en = overview_en.strip()
            if overview_en != '' and overview_en != 'null' and overview_en != '0':
                overview = f'Only in English - {overview_en}'
            else:
                overview = ''

        if overview != '':
            print(f'Overview: {overview}\n')
        else:
            print('Overview not available on TMD\n')


        key_trailer = ''
        lang_trailer = tmdb_idioma.upper()
        trailers_mylang = tmdb.Movies(tvg_tmdbid).videos(language=tmdb_idioma)['results']
        if len(trailers_mylang) > 0:
            key_trailer = trailers_mylang[0]['key']
            key_trailer = key_trailer.strip()
        else:
            trailers_en = tmdb.Movies(tvg_tmdbid).videos()['results']
            if len(trailers_en) > 0:
                key_trailer = trailers_en[0]['key']
                key_trailer = key_trailer.strip()
                lang_trailer = 'EN'

        if key_trailer != '':
            print(f'Trailer: {lang_trailer} | {URLYOUTUBE}{key_trailer}\n')
        else:
            print('Trailer not available on TMD\n')

    else:
        print('TMDB Movie ID not informed\n')

    print('==========================\n')

"""
#poster: ok, overview: pt-BR , trailer: pt-BR
movie_detail('24428')

#poster: ok, overview: pt-BR , trailer: English
movie_detail('89')

#poster: ok, overview: English , trailer: English
movie_detail('438890')

#poster: nothing, overview: English , trailer: nothing
movie_detail('740437')
"""


def serie_info(serieNome=''):
    if str(serieNome).strip() != '':
        search = tmdb.Search()
        r_tv = search.tv(query=serieNome, language=tmdb_idioma)
        if len(r_tv['results']) > 0:
            for item in r_tv['results']:
                print(item)

                '''
                source_img = item['poster_path']
                if source_img != None:
                    print('========================')   
                    print(source_img)
                    print('========================')

                '''
    else:
        print('Serie name not informed\n')
        
serie_info('A paranormal')
