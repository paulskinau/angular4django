import { Injectable } from '@angular/core';
import { Http, Response,Headers,RequestMethod, RequestOptions }          from '@angular/http';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import {Observable} from 'rxjs/Rx';


export interface RobotResponse {
    result: string;
    error: string;   
}

@Injectable()
export class RobotService {

  robotsUrl = "http://localhost:8000/api/robot/"

  constructor(private http: Http) { };

  getPath(terrain)
  {

  let headers = new Headers();

  let body = new FormData();
  body.append('terrain', terrain);

    let requestOptions = new RequestOptions({
        method: RequestMethod.Post,
        url: this.robotsUrl,
        headers: headers,
        body: body
    });

    return this.http.post(this.robotsUrl, body  )
                          .map(this.extractData)

  }

  private extractData(res: Response) {
    let body = res.json();
    if (body.error)
    {
      return body.error;
    }

    return body.result || { };
 

  }


}
