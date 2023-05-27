from .models import GenomeCharacteristics
import pandas as pd
import os

def detection(snp_filepath):

    #DB에 저장한 우리가 타게팅한 비만 유전자 SNP 목록 불러옴
    id_list = GenomeCharacteristics.objects.values_list('snp_id', flat=True)
    id_list = list(id_list)

    print("-------------------------------------------------------------------")
    print("다음의 비만 유전자 snp를 보유하고 있는지 확인합니다...")
    print(id_list)

    user_snp = pd.read_csv(snp_filepath)

    #사용자 genome SNP file에서 타게팅 비만 유전자 SNP rsid가 있는지 확인
    find_snp_list = []
    no_snp_list = []
    for rsid in id_list:
        find_snp = user_snp.loc[user_snp['# rsid'] == rsid]
        if find_snp.empty != True:
            find_snp_list.append(find_snp['# rsid'].values[0])
        else:
            no_snp_list.append(rsid)

    print("-------------------------------------------------------------------")
    print("사용자의 보유 SNP list")
    print(find_snp_list)
    print("사용자의 미보유 SNP list")
    print(no_snp_list)

    if os.path.isfile(snp_filepath):
        os.remove(snp_filepath)
        if os.path.isfile(snp_filepath) != True:
            print("파일이 삭제 되었습니다.")
    else:
        print("지우고자 하는 파일 없음")

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

    print("-------------------------------------------------------------------")
    print("다음 snp에 대한 정보가 전달됩니다.")
    info_list = []
    for item in result:
        info_list.append(item['id'])

    print(info_list)

    return result



