import {Injectable} from '@angular/core';
import {HttpService} from "./http.service";
import {User} from "../models/user.model";
import {Config} from "../../Config";
import {tap} from "rxjs/internal/operators";

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private httpService: HttpService) {
  }

  login(user: User) {
    return this.httpService.post(
      "/auth/login/",
      user
    ).pipe(
      tap((data: any) => {
        Config.accessToken = data.access_token;
        console.log(Config.accessToken);
      })
    );
  }
}
