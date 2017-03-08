import shapely
import itertools
import fiona
with fiona.drivers():
        with fiona.open('Z:/GIS/gtech734/LastTestshp.shp') as source:
            meta=source.meta

            with fiona.open('dissolve.shp','w',**meta) as output:
                e=sorted(source, key = lambda k: k['properties']['MYFLD'])
                for key, group in itertools.groupby(e, key=lambda x:x['properties']['MYFLD']):
                    properties, geo = zip(*[(feature['properties'],(feature['geometry'])) for feature in group])
                    output.write({'geometry':mapping(unary_union(geom)), 'properties': properties[0]})
                


