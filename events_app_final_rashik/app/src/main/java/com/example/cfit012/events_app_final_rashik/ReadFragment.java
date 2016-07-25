package com.example.cfit012.events_app_final_rashik;



import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;
import org.w3c.dom.Text;

public class ReadFragment extends Fragment {

    public ReadFragment() {
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

        view = inflater.inflate(R.layout.fragment_read, container, false);

        return view;
    }

    public void onViewCreated(View view, Bundle savedstate)
    {
        super.onViewCreated(view, savedstate);
        try
        {
            json.put("event_id","1");

        }
        catch(JSONException e) {
            e.printStackTrace();
        }
        String serverURL="http://192.168.3.3:8080/read";
        TextView r=(TextView)view.findViewById(R.id.readContent);
        PostJson pj=new PostJson(json,r);
        pj.execute(serverURL);

//        String ans=" Value is :"+" "+flag;
//        TextView t=(TextView)view.findViewById(R.id.readContent);
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
                try
                {
                    json.put("event_id","1");

                }
                catch(JSONException e) {
                    e.printStackTrace();
                }
                String serverURL="http://192.168.3.3:8080/read";
                TextView r=(TextView)view.findViewById(R.id.readContent);
                PostJson pj=new PostJson(json,r);
                pj.execute(serverURL);
//                flag+=1;
//                String ans=" Value is :"+" "+flag;
//                TextView t=(TextView)v.findViewById(R.id.readContent);
//                t.setText(ans);
            }
        }

    }


}
