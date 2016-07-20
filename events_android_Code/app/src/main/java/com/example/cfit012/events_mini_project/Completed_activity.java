package com.example.cfit012.events_mini_project;

import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class Completed_activity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_completed_activity);

        Intent intent=getIntent();

        String serverURL="http://192.168.0.113:8080/completed";
        new Completed().execute(serverURL);
    }

    protected class Completed extends AsyncTask<String ,Void,Void> {

        String output;

        protected Void doInBackground(String... urls) {
            try {

                URL url = new URL(urls[0]);
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestMethod("GET");
                conn.setRequestProperty("Accept", "application/json");

                if (conn.getResponseCode() != 200) {
                    throw new RuntimeException("Failed : HTTP error code : "
                            + conn.getResponseCode());
                }

                BufferedReader br = new BufferedReader(new InputStreamReader(
                        (conn.getInputStream())));


                //System.out.println("Output from Server .... \n");
                output="Output from Server .... "+"\n";
                String ans="";
                while ((ans= br.readLine()) != null) {
                    output+=ans+"\n";
                }

                conn.disconnect();

            } catch (MalformedURLException e) {

                e.printStackTrace();

            } catch (IOException e) {

                e.printStackTrace();

            }

            return null;
        }

        protected void onPostExecute(Void unused)
        {
            TextView t=(TextView)findViewById(R.id.text1);
            t.setText(output);
        }
    }
}
