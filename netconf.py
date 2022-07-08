import xmltodict
import json

dictionary = xmltodict.parse("""
       <TABLE_vlanbriefxbrief>
        <ROW_vlanbriefxbrief>
         <vlanshowbr-vlanid>1</vlanshowbr-vlanid>
         <vlanshowbr-vlanid-utf>1</vlanshowbr-vlanid-utf>
         <vlanshowbr-vlanname>default</vlanshowbr-vlanname>
         <vlanshowbr-vlanstate>active</vlanshowbr-vlanstate>
         <vlanshowbr-shutstate>noshutdown</vlanshowbr-shutstate>
         <vlanshowplist-ifidx>port-channel1,port-channel100,Ethernet1/46,Ethernet1/47,Ethernet1/48</vlanshowplist-ifidx>
        </ROW_vlanbriefxbrief>
        <ROW_vlanbriefxbrief>
         <vlanshowbr-vlanid>2</vlanshowbr-vlanid>
         <vlanshowbr-vlanid-utf>2</vlanshowbr-vlanid-utf>
         <vlanshowbr-vlanname>VLAN0002</vlanshowbr-vlanname>
         <vlanshowbr-vlanstate>active</vlanshowbr-vlanstate>
         <vlanshowbr-shutstate>noshutdown</vlanshowbr-shutstate>
         <vlanshowplist-ifidx>port-channel1,port-channel100,Ethernet1/46,Ethernet1/47,Ethernet1/48</vlanshowplist-ifidx>
        </ROW_vlanbriefxbrief>
       </TABLE_vlanbriefxbrief>
""")
""" json_object = json.dumps(dictionary) 
print(json_object) """

#print(dictionary["TABLE_vlanbriefxbrief"]["ROW_vlanbriefxbrief"])
vlaninfo=dictionary["TABLE_vlanbriefxbrief"]["ROW_vlanbriefxbrief"]#put the hiearacy here
vlanarray={}
for x in range(len(vlaninfo)):
    dct=vlaninfo[x]
    vlanarray[dct["vlanshowbr-vlanid"]]=dct["vlanshowplist-ifidx"].split(",")#will make list
#{'1': ['port-channel1', 'port-channel100', 'Ethernet1/46', 'Ethernet1/47', 'Ethernet1/48'], 
# '2': ['port-channel1', 'port-channel100', 'Ethernet1/46', 'Ethernet1/47', 'Ethernet1/48']}
#print(vlanarray)
# compare the keys in dict
vlanlist={"1":["port-channel1","port-channel100","Ethernet1/46","Ethernet1/47","Ethernet1/48"],"2":["port-channel22222222","port-channel100","Ethernet1/46","Ethernet1/47","Ethernet1/48"]}

flag=0
for x in vlanlist:
    check=True
    if x in vlanarray:
        continue
    else:
        print("Vlan "+x + " not existing")
        check=False
        flag+=1
if flag==0:
    print("Every vlan exist")
if flag!=0:
    exit()

#compare the value in dict
for x in vlanarray:
    check=True
    for y in vlanlist[x]:
        
        if y in vlanarray[x]:
            continue
        else:
            print("No, Vlan"+str(x)+" "+ str(y) +" is different")
            check=False
    if check==True:
        print("Vlan"+ str(x)+" has the right configuration")
