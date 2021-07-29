import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApioneService {

  baseurl = "http://127.0.0.1:8000";
  httpHeaders = new HttpHeaders({'Content-type':'applcation/json'})

  constructor(private http: HttpClient){ }

  getAllProfiles(): Observable<any>{
    return this.http.get(
      this.baseurl+'/user_profile/',
     {headers:this.httpHeaders});
  }
}
