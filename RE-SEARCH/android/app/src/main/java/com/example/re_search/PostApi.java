package com.example.re_search;

import com.example.re_search.model.User;
import com.example.re_search.model.Login;
import com.example.re_search.model.PostModel;
import java.util.List;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.DELETE;
import retrofit2.http.GET;
import retrofit2.http.Header;
import retrofit2.http.POST;
import retrofit2.http.PUT;
import retrofit2.http.Path;

public interface PostApi {


    //Use your own IPv4 address
    String root = "http://192.168.0.102:8000/";
//  String root = "http://127.0.0.1:8000/";


    String base_local = root + "api/";
    String BASE_URL = base_local + "";
    String POST_URL = base_local + "clusterapi/";
    String API_URL = root + "api/";



   @POST("api-token-auth/")
    Call<User> login(@Body Login login);

    @POST("registerapi/")
    Call<User> registrationUser(@Body User userModel);


    @GET("clusterapi/")
    Call<List<PostModel>> getListPost();


}