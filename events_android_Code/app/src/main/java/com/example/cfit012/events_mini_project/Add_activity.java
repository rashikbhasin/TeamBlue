package com.example.cfit012.events_mini_project;

import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class Add_activity extends AppCompatActivity {

    String output;

    JSONObject json=new JSONObject();


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_activity);

        Intent intent=getIntent();


        Button submit=(Button)findViewById(R.id.add);



        final EditText id=(EditText)findViewById(R.id.event_id);
        final EditText name=(EditText)findViewById(R.id.name);
        final EditText info=(EditText)findViewById(R.id.event_info);
        final EditText date=(EditText)findViewById(R.id.date);
        final EditText venue=(EditText)findViewById(R.id.venue);
        final EditText city=(EditText)findViewById(R.id.city);

        submit.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {

                try {
                    json.put("event_id",id.getText().toString());
                    json.put("name",name.getText().toString());
                    json.put("event_info",info.getText().toString());
                    json.put("date",date.getText().toString());
                    json.put("venue",venue.getText().toString());
                    json.put("city",city.getText().toString());

                } catch (JSONException e) {
                    e.printStackTrace();
                }

                String serverURL="http://192.168.0.113:8080/add";
                new Adding().execute(serverURL);

            }
        });
    }

    class Adding extends AsyncTask<String ,Void,Void> {

        TextView answer=(TextView)findViewById(R.id.output);

        protected Void doInBackground(String... urls)
        {
            try {


                URL url = new URL(urls[0]);
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setDoOutput(true);
                conn.setRequestMethod("POST");
                conn.setRequestProperty("Content-Type", "application/json");

                //String input = "{\"event_id\":\"3\",\"name\":\"aamya\",\"event_info\":\"info 3\",\"date\":\"2019-07-02\",\"venue\":\"venue 3\",\"city\":\"mumbai\"}";

                OutputStream os = conn.getOutputStream();


                //os.write(input.getBytes());
                os.write(json.toString().getBytes());
                os.flush();

                /*if (conn.getResponseCode() != HttpURLConnection.HTTP_CREATED) {
                        throw new RuntimeException("Failed : HTTP error code : "
                            + conn.getResponseCode());
                    }*/

                BufferedReader br = new BufferedReader(new InputStreamReader(
                        (conn.getInputStream())));

                String x="";
                output="";
                //System.out.println("Output from Server .... \n");
                while ((x = br.readLine()) != null) {
                    //System.out.println(output);
                    output=output+x+"\n";
                }

                conn.disconnect();

            }
            catch (IOException e) {

                e.printStackTrace();

            }
            return null;
        }

        protected void onPostExecute(Void unused)
        {
            answer.setText(output);
        }
    }
}
