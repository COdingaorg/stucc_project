import { Component } from '@angular/core';
import { ApioneService } from './apione.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers:[ApioneService]
})
export class AppComponent {
  title = 'stuccFrontend';
  profiles = [{'title':'titanic', 'runtime':'150mins'},{'title':'titanic 2', 'runtime':'250mins'} ];

  constructor(private api:ApioneService){
    this.getAllProfiles();
  }
  getAllProfiles = ()=>{
    this.api.getAllProfiles().subscribe(
      data => {
        this.profiles = data
      },
      error =>{
        console.log(error)
      }
    )
  }
}
