//Standard includes
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//DataTable
using System.Data;

// JSON Consumption
using System.Net;
using Newtonsoft.Json;

//CSV Saving
using System.IO;
using System.Text.RegularExpressions;


namespace GetEmbed_Consumer
{
    class Program
    {
        static DataTable AnalysisData = new DataTable();
        static void AddColumns()
        {
            AnalysisData.Columns.Add("ProgrammeID");
            AnalysisData.Columns.Add("ProjectID");
            AnalysisData.Columns.Add("PropertyCode");
            AnalysisData.Columns.Add("Completion Date");
            AnalysisData.Columns.Add("ProfileType");
            AnalysisData.Columns.Add("PropertyType");
            AnalysisData.Columns.Add("PrimaryEnergy");
            AnalysisData.Columns.Add("SpaceHeating");
            AnalysisData.Columns.Add("BER");
            AnalysisData.Columns.Add("SAP");
            AnalysisData.Columns.Add("PrimaryEnergy_Sensor");
            AnalysisData.Columns.Add("SpaceHeating_Sensor");
        }

        static void AddRow(string programmeid, string projectid, string propertycode, string primaryenergy, string spaceheating, 
            string ber, string sap , string completionDate , string profileType , string property_type,
            string PrimaryEnergySensor, string SpaceHeatingSensor)
        {
            DataRow r = AnalysisData.NewRow();
            r["ProgrammeID"] = programmeid;
            r["ProjectID"] = projectid;
            r["PropertyCode"] = propertycode;
            r["Completion Date"] = completionDate;
            r["ProfileType"] = profileType;
            r["PrimaryEnergy"] = primaryenergy;
            r["SpaceHeating"] = spaceheating;
            r["BER"] = ber;
            r["SAP"] = sap;
            r["PropertyType"] = property_type;
            r["PrimaryEnergy_Sensor"] = PrimaryEnergySensor;
            r["SpaceHeating_Sensor"] = SpaceHeatingSensor;
            AnalysisData.Rows.Add(r);
        }

        static void DataTableToCSV(DataTable dt)
        {
            StringBuilder sb = new StringBuilder();

            IEnumerable<string> columnNames = dt.Columns.Cast<DataColumn>().
                                              Select(column => column.ColumnName);
            sb.AppendLine(string.Join(",", columnNames));

            foreach (DataRow row in dt.Rows)
            {
                IEnumerable<string> fields = row.ItemArray.Select(field => field.ToString());
                sb.AppendLine(string.Join(",", fields));
            }

            File.WriteAllText("test.csv", sb.ToString());
        }

        static void Main(string[] args)
        {
            AddColumns();

            var syncClient = new WebClient(); //For Interaction With Webservice

            // Get data for each project within getembed
            string programme_id = "bfb6e716f87d4f1a333fd37d5c3679b2b4b6d87f";
            string apiProgramSource = "http://www.getembed.com/4/programmes/" + programme_id + "/projects/";
            var prjcontent = syncClient.DownloadString(apiProgramSource);
            List<Project.RootObject> projectDataList = new List<Project.RootObject>(JsonConvert.DeserializeObject<IEnumerable<Project.RootObject>>(prjcontent));

            // Get data for entity (project)
            foreach (Project.RootObject d in projectDataList)
            {
                string project_id = d.project_id;
                string apiProjectSource = "http://www.getembed.com/4/projects/" + d.project_id + "/entities/";
                var prjEntityContent = syncClient.DownloadString(apiProjectSource);
                
                Project.Entity.RootObject entityData = JsonConvert.DeserializeObject<Project.Entity.RootObject>(prjEntityContent);
                // foreach building
                foreach (var e in entityData.entities)
                {
                    string property_code = e.property_code;
                    string completion_date = ""; // = e.retrofit_completion_date.ToString();
                    string property_type = "";
                    string primaryEnergy_Sensor = "";
                    string spaceHeating_Sensor = "";
                    if (e.property_data != null) property_type = e.property_data.property_type;
                    
                    //foreach sensor we are interested in
                    foreach (var s in e.devices)
                    {
                        //if ( s ) primaryEnergy_Sensor = s.device_id;
                    }

                    //foreach building profile
                    foreach (var p in e.profiles)
                    {
                        string space_heating_requirement = p.profile_data.space_heating_requirement;
                        string total_primary_energy_requirement = p.profile_data.primary_energy_requirement;
                        string BER = p.profile_data.ber;
                        string SAP = p.profile_data.ter;
                        string profileType = p.profile_data.event_type;

                        AddRow(programme_id, project_id, property_code, total_primary_energy_requirement,
                            space_heating_requirement, BER, SAP, completion_date , profileType , property_type,
                            primaryEnergy_Sensor , spaceHeating_Sensor);
                    }
                }
            }

            // Datatable filled do something useful with it
            DataTableToCSV(AnalysisData);

        }
    }
}
