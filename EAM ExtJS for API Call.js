'[extensibleFramework] [tabName=HDR]': {
	beforesaverecord: function(a, b) {
	  var p = a.getFormPanel();          
	  console.log('beforesave')
	  /*GIS API Call*/

		var v_wo_data = {"WOData":[{"WO_Org":p.getFldValue("organization"),
									"WO_Code":p.getFldValue("workordernum"),
									"WO_Desc":p.getFldValue("description"),
									"WO_Type":p.getFldValue("workordertype"),
									"WO_Status":p.getFldValue("workorderstatus"),
									"WO_Class":p.getFldValue("woclass"),
									"WO_Dept":p.getFldValue("department"),
									"WO_Location":p.getFldValue("location"),
									"WO_Asset_Org":"*",
									"WO_Asset_OBType":"OSOBJA",
									"WO_Asset_Code":p.getFldValue("equipment")
									}]};

		//console.log(v_wo_data);


		var settings = {
		  "url": "https://eam-sqlquery.sapphire-cloud.net:8081/woapi",
		  "method": "POST",
		  "timeout": 0,
		  "headers": {
			"cid": "SPH",
			"tenant": "SSPLC_TRN",
			"Authorization": "Basic YWRtaW46YWRtaW4=",
			"Content-Type": "application/json"
		  },
		  "data": JSON.stringify(v_wo_data),
		};

		$.ajax(settings).done(function (response) {
		  console.log(response);
		});
					
		/*GIS API Call*/
	  
	  
	}
  },