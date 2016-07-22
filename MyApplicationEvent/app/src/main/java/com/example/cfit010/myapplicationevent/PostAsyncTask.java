package com.example.cfit010.myapplicationevent;

import android.os.AsyncTask;
import android.widget.TextView;

/**
 * Created by cfit010 on 22/7/16.
 */
public class PostAsyncTask extends AsyncTask<String ,Void,String> {

    private TextView textData;
    private String json_data;
    /*private TextView name;
    private TextView event_id;
    private TextView info;
    private TextView date;
    private TextView city;
    private TextView venue;*/

    public PostAsyncTask(TextView textData,String json_data){//(TextView name,TextView event_id, TextView info, TextView date, TextView city, TextView venue) {
        this.textData = textData;
        this.json_data = json_data;
        /*this.name = name;
        this.event_id = event_id;
        this.info = info;
        this.date = date;
        this.city = city;
        this.venue = venue;*/
    }


    protected String doInBackground(String... urls) {
        HttpRequest request = new HttpRequest();
        String result = request.doPost(urls[0],json_data);
        return result;
    }

    protected void onPostExecute(String result)
    {
        ParseJSON json_obj = new ParseJSON();
        String output = "";
        output = json_obj.parse(result);
        this.textData.setText(output);
    }
}