package com.example.cfit010.myapplicationevent.activities;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

import com.example.cfit010.myapplicationevent.R;

import org.json.JSONException;
import org.json.JSONObject;

/**
 * Created by cfit010 on 22/7/16.
 */
public class FormActivity  extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.city_activity);
    }

    public void openPostActivity(View view) {
        Intent intent = new Intent(FormActivity.this, PostActivity.class);

        EditText city = (EditText) findViewById(R.id.city);
        JSONObject obj = new JSONObject();
        try {

            obj.put("city", city.getText().toString());
        } catch (JSONException e) {
            e.printStackTrace();
        }
        intent.putExtra("json", obj.toString());
        String method = getIntent().getStringExtra("method");
        intent.putExtra("method", method);
        startActivity(intent);
    }
}