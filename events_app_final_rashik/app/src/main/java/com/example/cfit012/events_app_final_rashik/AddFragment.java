package com.example.cfit012.events_app_final_rashik;



import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;
import org.w3c.dom.Text;

public class AddFragment extends Fragment {

    public AddFragment() {
        // Required empty public constructor
    }

    private JSONObject json=new JSONObject();

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

//    static int flag = 0;
//    private static boolean isViewShown = false;

    static View view;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        view = inflater.inflate(R.layout.fragment_add, container, false);

        return view;
    }

    public void onViewCreated(View view, Bundle savedstate)
    {
        super.onViewCreated(view, savedstate);
        Button b=(Button)getView().findViewById(R.id.submit);

        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try
                {
                    EditText id=(EditText)getView().findViewById(R.id.addEventId);
                    EditText name=(EditText)getView().findViewById(R.id.addEventName);
                    EditText info=(EditText)getView().findViewById(R.id.addEventInfo);
                    EditText date=(EditText)getView().findViewById(R.id.addEventDate);
                    EditText venue=(EditText)getView().findViewById(R.id.addEventVenue);
                    EditText city=(EditText)getView().findViewById(R.id.addEventCity);


//                    json.put("event_id","3");
//                    json.put("name","aamya");
//                    json.put("event_info","info 3");
//                    json.put("date","2011-02-03");
//                    json.put("venue","venue 3");
//                    json.put("city","mumbai");
                    json.put("event_id",id.getText().toString());
                    json.put("name",name.getText().toString());
                    json.put("event_info",info.getText().toString());
                    json.put("date",date.getText().toString());
                    json.put("venue",venue.getText().toString());
                    json.put("city",city.getText().toString());

                }
                catch(JSONException e) {
                    e.printStackTrace();
                }
                String serverURL="http://192.168.3.3:8080/add";
                TextView answer=(TextView)getView().findViewById(R.id.newAdded);
                PostJson pj=new PostJson(json,answer);
                pj.execute(serverURL);
            }
        });

//        String ans=" Value is :"+" "+flag;
//        TextView t=(TextView)view.findViewById(R.id.addContent);
//        t.setText(ans);

    }

    @Override
    public void setUserVisibleHint(boolean visible)
    {
        super.setUserVisibleHint(visible);


        if (visible)
        {

            View v =  view ;
            if (v == null) {
                //Toast.makeText(getActivity(), "ERROR ", Toast.LENGTH_LONG ).show();
                return;
            }
            else
            {
                Button b=(Button)view.findViewById(R.id.submit);

                b.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View view) {
                        try
                        {
                            EditText id=(EditText)getView().findViewById(R.id.addEventId);
                            EditText name=(EditText)getView().findViewById(R.id.addEventName);
                            EditText info=(EditText)getView().findViewById(R.id.addEventInfo);
                            EditText date=(EditText)getView().findViewById(R.id.addEventDate);
                            EditText venue=(EditText)getView().findViewById(R.id.addEventVenue);
                            EditText city=(EditText)getView().findViewById(R.id.addEventCity);
                            json.put("event_id",id.getText().toString());
                            json.put("name",name.getText().toString());
                            json.put("event_info",info.getText().toString());
                            json.put("date",date.getText().toString());
                            json.put("venue",venue.getText().toString());
                            json.put("city",city.getText().toString());
//                            json.put("event_id","3");
//                            json.put("name","aamya");
//                            json.put("event_info","info 3");
//                            json.put("date","2011-02-03");
//                            json.put("venue","venue 3");
//                            json.put("city","mumbai");

                        }
                        catch(JSONException e) {
                            e.printStackTrace();
                        }
                        String serverURL="http://192.168.3.3:8080/add";
                        TextView answer=(TextView)getView().findViewById(R.id.newAdded);
                        PostJson pj=new PostJson(json,answer);
                        pj.execute(serverURL);
                    }
                });
            }
        }

    }


}
