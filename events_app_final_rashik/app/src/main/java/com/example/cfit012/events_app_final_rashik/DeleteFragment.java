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

public class DeleteFragment extends Fragment {

    public DeleteFragment() {
        // Required empty public constructor
    }

    private JSONObject json=new JSONObject();

    Button b;
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

        view = inflater.inflate(R.layout.fragment_delete, container, false);

        return view;
    }

    public void onViewCreated(View view, Bundle savedstate)
    {
        super.onViewCreated(view, savedstate);
        b=(Button)getView().findViewById(R.id.deleteButton);
        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try
                {
                    EditText ed=(EditText)getView().findViewById(R.id.deleteId);
                    json.put("event_id",ed.getText().toString());

                }
                catch(JSONException e) {
                    e.printStackTrace();
                }
                String serverURL="http://192.168.3.3:8080/deleted";
                TextView r=(TextView)getView().findViewById(R.id.deletedItem);
                PostJson pj=new PostJson(json,r);
                pj.execute(serverURL);

            }
        });



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
                //Button b=(Button)getView().findViewById(R.id.deleteButton);
                b.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View view) {
                        try
                        {
                            EditText ed=(EditText)getView().findViewById(R.id.deleteId);
                            json.put("event_id",ed.getText().toString());

                        }
                        catch(JSONException e) {
                            e.printStackTrace();
                        }
                        String serverURL="http://192.168.3.3:8080/deleted";
                        TextView r=(TextView)getView().findViewById(R.id.deletedItem);
                        PostJson pj=new PostJson(json,r);
                        pj.execute(serverURL);

                    }
                });

//                flag+=1;
//                String ans=" Value is :"+" "+flag;
//                TextView t=(TextView)v.findViewById(R.id.readContent);
//                t.setText(ans);
            }
        }

    }


}
