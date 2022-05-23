package com.example.re_search;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.KeyEvent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import com.example.re_search.model.PostModel;
import java.util.ArrayList;
import java.util.List;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;


public class Home extends Fragment{


    private ArrayList<Integer> pkPost = new ArrayList<>();
    private ArrayList<String> namePost = new ArrayList<>();
    private RecyclerView recyclerView;



    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {

        View rootView = inflater.inflate(R.layout.post_list, container, false);

        recyclerView = rootView.findViewById(R.id.recycler_category_list);



        if ( InternetUtil.isInternetOnline(getActivity()) ){
            ClearList();
            showAllPosts();
        }


        getActivity().setTitle("Clusters");

        return rootView;


    }

    private void showAllPosts() {

        Log.i("All posts showed", "All posts showed");
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl(PostApi.API_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .build();
        Log.i("Retrofit build", "Retrofit build");
        PostApi postApi= retrofit.create(PostApi.class);
        Log.i("Postapi createdd", "Postapi createdd");
        Call<List<PostModel>> call = postApi.getListPost();
        Log.i("Call list called", "Call list called");

        call.enqueue(new Callback<List<PostModel>>() {

            @Override
            public void onResponse(Call<List<PostModel>> call, Response<List<PostModel>> response) {

                Log.i("Response Received", "Response Received");
                if(response.isSuccessful()){

                    Log.i("Response Received", "Response Received");
                    if (response.body() != null) {
                        List<PostModel> postList = response.body();

                        for(PostModel h:postList){

                            //Integer cat_id = h.getId();
                            //pkPost.add(cat_id);

                            String cat_name = h.getTitle();
                            namePost.add(cat_name);


                        }

                        initRecyclerView();

                    }

                }else {
                    Log.d("fail", "fail");
                }
            }

            @Override
            public void onFailure(Call<List<PostModel>> call, Throwable t) {
                Log.d("fail", t.getMessage() == null ? "" : t.getMessage());
            }

        });

    }


    private void initRecyclerView(){
        Log.d("Home", "initRecyclerView: init recyclerview.");
        RecyclerHomeList adapter = new RecyclerHomeList(getActivity(), pkPost, namePost);
        recyclerView.setLayoutManager(new LinearLayoutManager(getActivity()));
        recyclerView.setAdapter(adapter);
    }


    public void ClearList()
    {
        pkPost.clear();
        namePost.clear();

        RecyclerHomeList adapter = new RecyclerHomeList(getActivity(), pkPost,  namePost);
        adapter.notifyDataSetChanged();
        recyclerView.setAdapter(adapter);
    }





    @Override
    public void onResume() {

        super.onResume();

        getView().setFocusableInTouchMode(true);
        getView().requestFocus();
        getView().setOnKeyListener(new View.OnKeyListener() {
            @Override
            public boolean onKey(View v, int keyCode, KeyEvent event) {
                if (event.getAction() == KeyEvent.ACTION_UP && keyCode == KeyEvent.KEYCODE_BACK){
                    getActivity().finish();
                    return true;
                }
                return false;
            }
        });
    }




}