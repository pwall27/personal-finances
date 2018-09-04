import {Injectable} from '@angular/core';
import {HttpService} from "./http.service";
import {User} from "../models/user.model";
import {Config} from "../../Config";
import {tap} from "rxjs/internal/operators";
import {JwtHelperService} from "@auth0/angular-jwt";
import {isNullOrUndefined} from "util";

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private httpService: HttpService) {
  }

  login(user: User) {
    return this.httpService.post(
      "/auth/login/",
      user
    ).pipe(
      tap((data: any) => {
        Config.accessToken = data.access_token;
      })
    );
  }

  logout() {
    Config.accessToken = null;
  }

  isAuthenticated() {
    const helper = new JwtHelperService();
    return !isNullOrUndefined(Config.accessToken ) && !helper.isTokenExpired(Config.accessToken);
  }
}
