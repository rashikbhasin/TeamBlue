package com.example.cfit010.myapplicationevent.activities;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

import com.example.cfit010.myapplicationevent.GetAsyncTask;
import com.example.cfit010.myapplicationevent.HttpRequest;
import com.example.cfit010.myapplicationevent.PostAsyncTask;
import com.example.cfit010.myapplicationevent.R;

/**
 * Created by cfit010 on 22/7/16.
 */
public class PostActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.city_activity);
        TextView name=(TextView)findViewById(R.id.output);
        String method = getIntent().getStringExtra("method");
        String url = new HttpRequest().url;
        String json = getIntent().getStringExtra("json");
        PostAsyncTask get_request = new PostAsyncTask(name,json);
        get_request.execute(url+"/"+method);
    }


}
