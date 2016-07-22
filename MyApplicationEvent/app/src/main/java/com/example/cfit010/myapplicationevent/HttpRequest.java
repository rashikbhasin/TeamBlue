package com.example.cfit010.myapplicationevent;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;


public class HttpRequest {


    public static String url = "http://192.168.3.6:8080";

    public String doGet(String url_request)
    {
        HttpURLConnection conn = null;
        try {

            URL url = new URL(url_request);//http://127.0.0.1:5000/ //http://www.httpbin.org/get
            conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setRequestProperty("Accept", "application/json");

            /*if (conn.getResponseCode() != 201) {
                throw new RuntimeException("Failed : HTTP error code : "
                        + conn.getResponseCode());
            }*/

            BufferedReader br = new BufferedReader(new InputStreamReader(
                    (conn.getInputStream())));

            String output;
            String result="";
            while ((output = br.readLine()) != null) {
                result = result+output;
            }

            return result;

        } catch (Exception ignored) {

        }
        finally {
            assert conn != null;
            conn.disconnect();
        }
        return "Error";
    }

    public String doPost(String url_request, String json_data)
    {
        HttpURLConnection conn = null;
        try {

            URL url = new URL(url_request);//"http://192.168.3.10:8000/create_contact"
            conn = (HttpURLConnection) url.openConnection();
            conn.setDoOutput(true);
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json");

            System.out.println(json_data);

            OutputStream os = conn.getOutputStream();
            os.write(json_data.getBytes());
            os.flush();

			/*if (conn.getResponseCode() != HttpURLConnection.HTTP_CREATED) {
			throw new RuntimeException("Failed : HTTP error code : "
				+ conn.getResponseCode());
		}*/

            BufferedReader br = new BufferedReader(new InputStreamReader(
                    (conn.getInputStream())));

            String output;
            String result = "";

            //AddContactActivity.this


            while ((output = br.readLine()) != null) {
                result = result+output;
            }
            return result;
        } catch (Exception ignored) {

        }
        finally {
            assert conn != null;
            conn.disconnect();
        }
        return "Error";
    }
}