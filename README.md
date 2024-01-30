# Pear Flowering-date Prediction model

신고 배 만개일 예측 모델(DVR, mDVR, CD): [demo.ipynb](https://github.com/riverallzero/pear_flowering/blob/main/demo.ipynb)

```pip install git+https://github.com/riverallzero/pear_flowering.git```

```python
from pear_flowering import location, dvr, mdvr, cd

# 지역번호 검색
year = 2023
loc = location("전주")

# 개화일 예측
dvr_result = dvr(year, loc)
mdvr_result = mdvr(year, loc)
cd_result = cd(year, loc)

print(f"DVR: {dvr_result}, mDVR: {mdvr_result}, CD: {cd_result}")
```

## loc(지역번호)

```
'90-속초', '93-북춘천', '95-철원', '98-동두천', '99-파주', '100-대관령', '101-춘천', '102-백령도', '104-북강릉', '105-강릉', '106-동해',
'108-서울', '112-인천', '114-원주', '115-울릉도', '116-관악산', '119-수원', '121-영월', '127-충주', '129-서산', '130-울진', '131-청주',
'133-대전', '135-추풍령', '136-안동', '137-상주', '138-포항', '140-군산', '143-대구', '146-전주', '152-울산', '155-창원', '156-광주',
'159-부산', '162-통영', '164-무안', '165-목포', '168-여수', '169-흑산도', '170-완도', '172-고창', '174-순천', '175-진도(첨찰산)',
'176-대구(기)', '177-홍성', '184-제주', '185-고산', '187-성산', '188-성산', '189-서귀포', '192-진주', '201-강화', '202-양평',
'203-이천','211-인제', '212-홍천', '214-삼척', '216-태백', '217-정선군', '221-제천', '226-보은', '232-천안', '235-보령', '236-부여',
'238-금산', '239-세종', '243-부안', '244-임실', '245-정읍', '247-남원', '248-장수', '251-고창군', '252-영광군', '253-김해시', '254-순창군',
'255-북창원','256-주암', '257-양산시', '258-보성군', '259-강진군', '260-장흥', '261-해남','262-고흥', '263-의령군', '264-함양군', '265-성산포',
'266-광양시', '268-진도군','271-봉화', '272-영주', '273-문경', '276-청송군', '277-영덕', '278-의성','279-구미', '281-영천',
'283-경주시', '284-거창', '285-합천', '288-밀양', '289-산청', '294-거제', '295-남해'
```

## ToDo
- [ ] mDVR 내생휴면종료일(현재 2.15 지정) 계산
- [ ] CD 내생휴면종료일(현재 2.15 지정) 계산
- [X] 지역 검색 함수 추가
      
