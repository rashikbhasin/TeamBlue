package com.example.cfit010.myapplicationevent.activities;

import android.app.Activity;
import android.app.DatePickerDialog;
import android.app.Dialog;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.View;
import android.widget.DatePicker;
import android.widget.EditText;
import com.example.cfit010.myapplicationevent.R;
import org.json.JSONException;
import org.json.JSONObject;

import java.text.SimpleDateFormat;
import java.util.Calendar;


/**
 * Created by cfit010 on 22/7/16.
 */
public class DateActivity extends Activity {

    static final int DATE_DIALOG_ID = 0;
    private int mYear,mMonth,mDay;
    EditText editText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.date_activity);

        Calendar c=Calendar.getInstance();
        mYear=c.get(Calendar.YEAR);
        mMonth=c.get(Calendar.MONTH);
        mDay=c.get(Calendar.DAY_OF_MONTH);
        //String dateFormat = "dd/MM/yyyy";
        editText = (EditText) findViewById(R.id.date);
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
        editText.setText(sdf.format(c.getTime()));

        editText.setOnClickListener(new View.OnClickListener() {


            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                showDialog(DATE_DIALOG_ID);

            }
        });

    }


    protected Dialog onCreateDialog(int id) {
        switch (id) {
            case DATE_DIALOG_ID:
                return new DatePickerDialog(this,
                        mDateSetListener,
                        mYear, mMonth, mDay);

        }

        return null;

    }
    private DatePickerDialog.OnDateSetListener mDateSetListener = new DatePickerDialog.OnDateSetListener() {

        public void onDateSet(DatePicker view, int year, int monthOfYear,
                              int dayOfMonth) {
            mYear = year;
            mMonth = monthOfYear;
            mDay = dayOfMonth;
            editText.setText(new StringBuilder().append(mDay).append("/").append(mMonth+1).append("/").append(mYear));

        }

    };



    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.activity_main_drawer, menu);
        return true;
    }


    public void openDateActivity(View view) {
        Intent intent = new Intent(DateActivity.this, PostDateActivity.class);

        JSONObject obj = new JSONObject();
        String month = "";
        String day = "";
        if(mMonth<10)
        {
            month = "0"+String.valueOf(mMonth+1);
        }
        else
        {
            month = String.valueOf(mMonth);
        }
        if(mDay<10)
        {
            day = "0"+String.valueOf(mDay);
        }
        else
        {
            day = String.valueOf(mDay);
        }
        String date = String.valueOf(mYear)+"-"+month+"-"+day;
        try {

            obj.put("date", date);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        intent.putExtra("json", obj.toString());
        String method = getIntent().getStringExtra("method");
        intent.putExtra("method", method);
        startActivity(intent);
    }
}
