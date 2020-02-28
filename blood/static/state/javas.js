$(document).ready(function(){

    //let's create arrays
    var AndhraPradesh = [{display: "Anantapur", value: "Anantapur" },
                          {display: "Chittoor", value: "Chittoor" },
                          {display: "East Godavari", value: "East Godavari" },
                          {display: "Guntur", value: "Guntur" },
                          {display: "Krishna", value: "Krishna" },
                          {display: "Kurnool", value: "Kurnool" },
                          {display: "Nellore", value: "Nellore" },
                          {display: "Prakasam", value: "Prakasam" },
                          {display: "Srikakulam", value: "Srikakulam" },
                          {display: "Visakhapatnam", value: "Visakhapatnam" },
                          {display: "Vizianagaram", value: "Vizianagaram" },
                          {display: "West Godavari", value: "West Godavari" },
                          {display: "YSR Kadapa", value: "YSR Kadapa" }];
    
    var ArunachalPradesh= [{display: "Tawang", value: "Tawang" },
    {display: "West Kameng", value: "West Kameng" },
    {display: "East Kameng", value: "East Kameng" },
    {display: "West Kameng", value: "West Kameng" },
    {display: "Papum Pare", value: "Papum Pare" },
    {display: "Kurung Kumey", value: "Kurung Kumey" },
    {display: "Kra Daadi", value: "Kra Daadi" },
    {display: "Lower Subansiri", value: "Lower Subansiri" },
    {display: "Upper Subansiri", value: "Upper Subansiri" },
    {display: "West Siang", value: "West Siang" }
    ,{display: "East Siang", value: "East Siang" },
    {display: "Siang", value: "Siang" },
    {display: "Upper Siang", value: "Upper Siang" },
    {display: "Lower Siang", value: "Lower Siang" },
    {display: "Lower Dibang Valley", value: "Lower Dibang Valley" },
    {display: "Dibang Valley", value: "Dibang Valley" },
    {display: "Anjaw", value: "Anjaw" },
    {display: "Lohit", value: "Lohit" },
    {display: "Namsai", value: "Namsai" },
    {display: "Changlang", value: "Changlang" },
    {display: "Tirap", value: "Tirap" },
    {display: "Longding", value: "Longding" }];	
    
    var Assam= [{display: "Tawang", value: "Tawang" },
    {display: "Baksa", value: "Baksa" },
    {display: "Barpeta", value: "Barpeta" },
    {display: "Biswanath", value: "Biswanath" },
    {display: "Bongaigaon", value: "Bongaigaon" },
    {display: "Cachar", value: "Cachar" },
    {display: "Charaideo", value: "Charaideo" },
    {display: "Chirang", value: "Chirang" },
    {display: "Darrang", value: "Darrang" },
    {display: "Dhemaji", value: "Dhemaji" },
    {display: "Dhubri", value: "Dhubri" },
    {display: "Dibrugarh", value: "Dibrugarh" },
    {display: "Goalpara", value: "Goalpara" },
    {display: "Golaghat", value: "Golaghat" },
    {display: "Hailakandi", value: "Hailakandi" },
    {display: "Hojai", value: "Hojai" },
    {display: "Jorhat", value: "Jorhat" },
    {display: "Kamrup Metropolitan", value: "Kamrup Metropolitan" },
    {display: "Kamrup", value: "Kamrup" },
    {display: "Karbi Anglong", value: "Karbi Anglong" },
    {display: "Karimganj", value: "Karimganj" },
    {display: "Kokrajhar", value: "Kokrajhar" },
    {display: "Lakhimpur", value: "Lakhimpur" },
    {display: "Majuli", value: "Majuli" },
    {display: "Morigaon", value: "Morigaon" },
    {display: "Nagaon", value: "Nagaon" },
    {display: "Nalbari", value: "Nalbari" },
    {display: "Dima Hasao", value: "Dima Hasao" },
    {display: "Sivasagar", value: "Sivasagar" },
    {display: "Sonitpur", value: "Sonitpur" },
    {display: "South Salmara-Mankachar", value: "South Salmara-Mankachar" },
    {display: "Tinsukia", value: "Tinsukia" },
    {display: "Udalguri", value: "Udalguri" },
    {display: "West Karbi Anglong", value: "West Karbi Anglong" }];
    
    var Bihar= [{display: "Araria", value: "Araria" },
    {display: "Arwal", value: "Arwal" },
    {display: "Aurangabad", value: "Aurangabad" },
    {display: "Banka", value: "Banka" },
    {display: "Begusarai", value: "Begusarai" },
    {display: "Bhagalpur", value: "Bhagalpur" },
    {display: "Bhojpur", value: "Bhojpur" },
    {display: "Buxar", value: "Buxar" },
    {display: "Darbhanga", value: "Darbhanga" },
    {display: "East Champaran (Motihari)", value: "East Champaran (Motihari)" },
    {display: "Gaya", value: "Gaya" },
    {display: "Gopalganj", value: "Gopalganj" },
    {display: "Jamui", value: "Jamui" },
    {display: "Jehanabad", value: "Jehanabad" },
    {display: "Kaimur (Bhabua)", value: "Kaimur (Bhabua)" },
    {display: "Katihar", value: "Katihar" },
    {display: "Khagaria", value: "Khagaria" },
    {display: "Kishanganj", value: "Kishanganj" },
    {display: "Lakhisarai", value: "Lakhisarai" },
    {display: "Madhepura", value: "Madhepura" },
    {display: "Madhubani", value: "Madhubani" },
    {display: "Munger (Monghyr)", value: "Munger (Monghyr)" },
    {display: "Muzaffarpur", value: "Muzaffarpur" },
    {display: "Nalanda", value: "Nalanda" },
    {display: "Nawada", value: "Nawada" },
    {display: "Patna", value: "Patna" },
    {display: "Purnia (Purnea)", value: "Purnia (Purnea)" },
    {display: "Rohtas", value: "Rohtas" },
    {display: "Saharsa", value: "Saharsa" },
    {display: "Samastipur", value: "Samastipur" },
    {display: "Saran", value: "Saran" },
    {display: "Sheikhpura", value: "Sheikhpura" },
    {display: "Sheohar", value: "Sheohar" },
    {display: "Sitamarhi", value: "Sitamarhi" },
    {display: "Siwan", value: "Siwan" },
    {display: "Supaul", value: "Supaul" },
    {display: "Vaishali", value: "Vaishali" },
    {display: "West Champaran", value: "West Champaran" }];
    
    var Chhattisgarh= [{display: "Tawang1", value: "Tawang1" }];
    var Chandigarh= [{display: "Tawang1", value: "Tawang1" }];
    var DadraandNagarHaveli= [{display: "Tawang2", value: "Tawang2" }];
    var DamanandDiu= [{display: "Tawang", value: "Tawang" }];
    var Gujarat= [{display: "Tawang", value: "Tawang" }];
    var Delhi= [{display: "Tawang", value: "Tawang" }];
    var Goa= [{display: "Tawang", value: "Tawang" }];
    var Haryana= [{display: "Tawang", value: "Tawang" }];
    var Gujarat= [{display: "Tawang", value: "Tawang" }];
    var HimachalPradesh= [{display: "Tawang", value: "Tawang" }];
    var JammuandKashmir= [{display: "Tawang", value: "Tawang" }];
    var Jharkhand= [{display: "Tawang", value: "Tawang" }];
    var Karnataka= [{display: "Tawang", value: "Tawang" }];
    var Kerala= [{display: "Tawang", value: "Tawang" }];
    var MadhyaPradesh= [{display: "Tawang", value: "Tawang" }];
    var Maharashtra= [{display: "Tawang", value: "Tawang" }];
    var Manipur= [{display: "Tawang", value: "Tawang" }];
    var Meghalaya= [{display: "Tawang", value: "Tawang" }];
    var Mizoram= [{display: "Tawang", value: "Tawang" }];
    var Nagaland= [{display: "Tawang", value: "Tawang" }];
    var Orissa= [{display: "Tawang", value: "Tawang" }];
    var Punjab= [{display: "Tawang", value: "Tawang" }];
    var Pondicherry= [{display: "Tawang", value: "Tawang" }];
    var Rajasthan= [{display: "Tawang", value: "Tawang" }];
    var Sikkim= [{display: "Tawang", value: "Tawang" }];
    var TamilNadu= [{display: "Tawang", value: "Tawang" }];
    var Tripura= [{display: "Tawang", value: "Tawang" }];
    var UttarPradesh= [{display: "Gorakhpur", value: "Gorakhpur" }];
    var Tripura= [{display: "Tawang", value: "Tawang" }];
    var Uttarakhand= [{display: "Tawang", value: "Tawang" }];
    var WestBengal= [{display: "Tawang", value: "Tawang" }];
    
    
    //If parent option is changed
    $("#parent_selection").change(function() {
            var parent = $(this).val(); //get option value from parent 
            
            switch(parent){ //using switch compare selected option and populate child
                  case 'Andhra Pradesh':
                     list(AndhraPradesh);
                    break;
                  case 'Arunachal Pradesh':
                     list(ArunachalPradesh);
                    break;				
                  case 'Assam':
                     list(Assam);
                    break;	
                  case 'Bihar':
                     list(Bihar);
                    break;
                  case 'Chhattisgarh':
                     list(Chhattisgarh);
                    break;				
                  case 'Chandigarh':
                     list(Chandigarh);
                    break;	
                  case 'Dadra and Nagar Haveli':
                     list(DadraandNagarHaveli);
                    break;
                  case 'Daman and Diu':
                     list(DamanandDiu);
                    break;				
                  case 'icecreams':
                     list(icecreams);
                    break;	
                  case 'Delhi':
                     list(Delhi);
                    break;
                  case 'Goa':
                     list(Goa);
                    break;				
                      
                  case 'Gujarat':
                     list(Gujarat);
                    break;
                              
                  
                 case 'Haryana':
                     list(Haryana);
                    break;
                  case 'Himachal Pradesh':
                     list(HimachalPradesh);
                    break;				
                  case 'Jammu and Kashmir':
                     list(JammuandKashmir);
                    break;	
                  case 'Jharkhand':
                     list(Jharkhand);
                    break;
                  case 'Karnataka':
                     list(Karnataka);
                    break;				
                  case 'Kerala':
                     list(Kerala);
                    break;	
                 case 'Madhya Pradesh':
                     list(MadhyaPradesh);
                    break;
                  case 'Maharashtra':
                     list(Maharashtra);
                    break;				
                  case 'Manipur':
                     list(Manipur);
                    break;	
    
                    
                 case 'Meghalaya':
                     list(Meghalaya);
                    break;
                  case 'Mizoram':
                     list(Mizoram);
                    break;				
                  case 'Nagaland':
                     list(Nagaland);
                    break;	
                 case 'Orissa':
                     list(Orissa);
                    break;
                    case 'Punjab':
                     list(Punjab);
                    break;
                  case 'Pondicherry':
                     list(Pondicherry);
                    break;				
                  case 'Rajasthan':
                     list(Rajasthan);
                    break;	
                 case 'Sikkim':
                     list(Sikkim);
                    break;
                    case 'Tamil Nadu':
                     list(TamilNadu);
                    break;
                  case 'Tripura':
                     list(Tripura);
                    break;				
                  case 'Uttar Pradesh':
                     list(UttarPradesh);
                    break;	
                 case 'Uttarakhand':
                     list(Uttarakhand);
                    break;
                case 'West Bengal':
                     list(WestBengal);
                    break;
                  
                    
                default: //default child option is blank
                    $("#child_selection").html('');	 
                    break;
               }
    });
    
    //function to populate child select box
    function list(array_list)
    {
        $("#child_selection").html(""); //reset child options
        $(array_list).each(function (i) { //populate child options 
            $("#child_selection").append("<option value=\""+array_list[i].value+"\">"+array_list[i].display+"</option>");
        });
    }
    
    });