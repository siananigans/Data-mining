##### Te categorical changing taking forever to run so like run it once and save the new data set and dont call it again otherwise itll timeout takes 4EVA
import pandas
import matplotlib.pyplot

#del null values
def drop_all_nulls(data):
	data = data.dropna()
	return(data)

#drop dupliactes
def drop_dup(data):
    data.drop_duplicates()
    return data

#drop unwanted attributes
def drop_unused_attributes(data):
	del_attributes = ['nametype', 'name', 'id','GeoLocation', 'mass']
	data = data.drop(columns = del_attributes)
	return(data)




#def catch_cate(data):
    #r=data['recclass']
    #i=0
    #for row in r:
      #  if row!= 'S' or 'SI' or 'I' or 'O':
     #       data=data.replace(to_replace=r.iloc[i], value='O')
    #    i=i+1
   # return data
        
			
#set categorical to values
#def class_spec(data):
    #r=data['recclass'].astype(str)
    #count=0
    #for i in range (0,len(r-1)):
        #result=cate_label(r.iloc[i])
        #print("Result",result)
        #if result=='S':
         #   data=data.replace(to_replace=r.iloc[i], value=result)
        #elif result=='SI':
        #    data=data.replace(to_replace=r.iloc[i], value=result)
       # elif result=='I':
      #      data=data.replace(to_replace=r.iloc[i], value=result)
     #   else:
    #        data=data.replace(to_replace=r.iloc[i], value='O')
   #     print(i)
  #      i=i+1
   
 #   return data

#def cate_label(recclass):
    	#def test(data):
		#main_meteorite_classes = {
		#["CI", "CM", "CO", "CV", "CK", "CR", "CH", "CB", "H", "L", "LL", "E", "OC", "LLL", "HL", "EH", "EL", "R", "K", "ACAPULCOITE", "LODRANITE", "WINONAITE", "HOWARDITE", "EUCRITE", "DIOGENITE", "ANGRITE", "AUBRITE", "UREILITE", "BRACHINITE", "LUNAR", "SHERGOTTITE", "NAKHLITE", "CHASSIGNITE", "MARTIAN", "ACHONDRITE", "CHONDRITE", "RELICTOC"]:'S',
		#["PALLASITE", "MESOSIDERITE"]:'SI',
		#["IC", "IIAB", "IIC", "IID", "IIF", "IIG", "IIIAB", "IIIE", "IIIF", "IVA", "IVB", "IAB", "UDEI", "PITTS", "sLL", "sLM", "sLH", "sHL", "sHH", "IIE"]:'I'
		#}
		#data=data.replace(["CI", "CM", "CO", "CV", "CK", "CR", "CH", "CB", "H", "L", "LL", "E", "OC", "LLL", "HL", "EH", "EL", "R", "K", "ACAPULCOITE", "LODRANITE", "WINONAITE", "HOWARDITE", "EUCRITE", "DIOGENITE", "ANGRITE", "AUBRITE", "UREILITE", "BRACHINITE", "LUNAR", "SHERGOTTITE", "NAKHLITE", "CHASSIGNITE", "MARTIAN", "ACHONDRITE", "CHONDRITE", "RELICTOC"],'S')
		#data=data.replace(to_replace=["PALLASITE", "MESOSIDERITE"],value='SI')
		#data=data.replace(to_replace=["IC", "IIAB", "IIC", "IID", "IIF", "IIG", "IIIAB", "IIIE", "IIIF", "IVA", "IVB", "IAB", "UDEI", "PITTS", "sLL", "sLM", "sLH", "sHL", "sHH", "IIE"],value='I')
		#d={"H6":'S','L5':'S'}#"CM":'S',"CO":'S',"CV":'S',"CK":'S',"CR":'S',"CH":'S',"CB":'S',"H":'S',"L":'S',"LL":'S',"E":'S',"OC":'S',"LLL":'S',"HL":'S',"EH":'S',"EL":'S',"R":'S',"K":'S',"ACAPULCOITE":'S',"LODRANITE":'S',"WINONAITE":'S',"HOWARDITE":'S',"EUCRITE":'S',"DIOGENITE":'S',"ANGRITE":'S',"AUBRITE":'S',"UREILITE":'S',"BRACHINITE":'S',"LUNAR":'S',"SHERGOTTITE":'S',"NAKHLITE":'S',"CHASSIGNITE":'S',"MARTIAN":'S',"ACHONDRITE":'S',"CHONDRITE":'S',"RELICTOC":'S',
		#"PALLASITE":'SI',"MESOSIDERITE":'SI',
		#"IC":'I',"IIAB":'I',"IIC":'I',"IID":'I',"IIF":'I',"IIG":'I',"IIIAB":'I',"IIIE":'I',"IIIF":'I',"IVA":'I',"IVB":'I',"IAB":'I',"UDEI":'I',"PITTS":'I',"sLL":'I',"sLM":'I',"sLH":'I',"sHL":'I',"sHH":'I',"IIE":'I'}
		#data=data.replace(d)
		#print(data)
	#main_meteorite_classes = {
	#	"S": ["CI", "CM", "CO", "CV", "CK", "CR", "CH", "CB", "H", "L", "LL", "E", "OC", "LLL", "HL", "EH", "EL", "R", "K", "ACAPULCOITE", "LODRANITE", "WINONAITE", "HOWARDITE", "EUCRITE", "DIOGENITE", "ANGRITE", "AUBRITE", "UREILITE", "BRACHINITE", "LUNAR", "SHERGOTTITE", "NAKHLITE", "CHASSIGNITE", "MARTIAN", "ACHONDRITE", "CHONDRITE", "RELICTOC"],
	#	"SI": ["PALLASITE", "MESOSIDERITE"],
	#	"I": ["IC", "IIAB", "IIC", "IID", "IIF", "IIG", "IIIAB", "IIIE", "IIIF", "IVA", "IVB", "IAB", "UDEI", "PITTS", "sLL", "sLM", "sLH", "sHL", "sHH", "IIE"]
	#}
	#get category 
	#take away uppercase
	#recclassNew = "".join(char for char in recclass if char.isalpha())
	#print(recclassNew)
	#S=[]
	#SI=[]
	#I=[]
	#O=[]
		
	#if 'iron' in recclassNew.lower():   
     #       I.append(recclassNew)
      #      return 'I'

	#for key in main_meteorite_classes.keys():
     #       if (recclassNew.upper() in main_meteorite_classes[key]):
        #            S.append(recclassNew)
      ##              return key
         #   for name in main_meteorite_classes[key]:
		#		    if (len(name) >= 3 and name in recclassNew.upper()):
         #               SI.append(recclassNew)
		#			    return key
    #return "O"


def main():
    #read in csv file
    data = pandas.read_csv('meteorite-landings.csv')

    
    #drop null values
    data_dropnull = drop_all_nulls(data)
    
    #remove dups
    data= drop_dup(data_dropnull)
    
    #del useless attributes to save time
    data_unused=drop_unused_attributes(data)
    

    
    #set back to var data
    data=data_unused
    
    #change cate data
    #data=class_spec(data)
    #doeant work
    #doesnt catch all the types 
    #data=data.replace(["CI", "CM", "CO", "CV", "CK", "CR", "CH", "CB", "H", "L", "LL", "E", "OC", "LLL", "HL", "EH", "EL", "R", "K", "ACAPULCOITE", "LODRANITE", "WINONAITE", "HOWARDITE", "EUCRITE", "DIOGENITE", "ANGRITE", "AUBRITE", "UREILITE", "BRACHINITE", "LUNAR", "SHERGOTTITE", "NAKHLITE", "CHASSIGNITE", "MARTIAN", "ACHONDRITE", "CHONDRITE", "RELICTOC"],'S')
    #data=data.replace(["PALLASITE", "MESOSIDERITE"],'SI')
    #data=data.replace(["IC", "IIAB", "IIC", "IID", "IIF", "IIG", "IIIAB", "IIIE", "IIIF", "IVA", "IVB", "IAB", "UDEI", "PITTS", "sLL", "sLM", "sLH", "sHL", "sHH", "IIE"],'I')
    
    #catch
    #data=catch_cate(data)
    
    #splitdata80:20
    copydata = data.copy()
    train_set = copydata.sample(frac=0.80, random_state=0)
    test_set = copydata.drop(train_set.index)
    #print(train_set)
    #print((train_set))
    #print(train_set.max(axis = 0))
    #print(train_set.head(10))
    #print(train_set.shape)
    print(len(test_set))
    return test_set


if __name__ == '__main__':
	main()