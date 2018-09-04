import {isNullOrUndefined} from "util";
import {environment} from "./environments/environment";

export class Config {
    // TODO: Set apiUrl based on environment
    static apiUrl = environment['baseUrl'];
    private _accessToken: string;

    static get accessToken(): string {
        return localStorage.getItem('accessToken');
    }

    static set accessToken(newAccessToken: string) {
      if(isNullOrUndefined(newAccessToken)){
        localStorage.removeItem('accessToken');
      } else{
        localStorage.setItem('accessToken', newAccessToken);
      }
    }
}
