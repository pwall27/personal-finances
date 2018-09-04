import {isNullOrUndefined} from "util";

export class Config {
    // TODO: Set apiUrl based on environment
    static apiUrl = "http://localhost:8000/api/v1";
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
