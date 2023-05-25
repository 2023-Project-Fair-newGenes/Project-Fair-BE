from .models import GenomeCharacteristics
import pandas as pd

def detection(snp_filepath):

    #DB에 저장한 우리가 타게팅한 비만 유전자 SNP 목록 불러옴
    id_list = GenomeCharacteristics.objects.values_list('snp_id', flat=True)
    id_list = list(id_list)

    user_snp = pd.read_csv(snp_filepath)

    #사용자 genome SNP file에서 타게팅 비만 유전자 SNP rsid가 있는지 확인
    find_snp_list = []
    for rsid in id_list:
        find_snp = user_snp.loc[user_snp['# rsid'] == rsid]
        if find_snp.empty != True:
            find_snp_list.append(find_snp['# rsid'].values[0])

    return find_snp_list

def getCharacteristic(find_snp_list):
    result = []
    for _rsid in find_snp_list:
        dict = {}
        info = GenomeCharacteristics.objects.get(snp_id=_rsid)
        dict['id'] = _rsid
        dict['snp_name'] = info.snp_name
        dict['characteristics'] = info.characteristics
        result.append(dict)

    return result



