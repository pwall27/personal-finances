import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Config} from "../../Config";


@Injectable()
export class HttpService {
    static API_BASE_URL: string = Config.apiUrl;

    constructor(protected _http: HttpClient) {
    }

    public get_assets(url: string) {
        return this._http.get(url);
    }

    public get(api_url: string) {
        let headers = this.setHeader();
        let url = HttpService.API_BASE_URL + api_url;
        return this._http.get(url, {headers: headers});
    }

    public post(api_url: string, data?: {}) {
        let headers = this.setHeader();
        let _data = JSON.stringify(data);
        let url = HttpService.API_BASE_URL + api_url;
        return this._http.post(url, _data, {headers: headers});
    }

    public patch(api_url: string, data?: {}) {
        let headers = this.setHeader();
        let _data = JSON.stringify(data);
        let url = HttpService.API_BASE_URL + api_url;
        return this._http.patch(url, _data, {headers: headers});
    }

    public put(api_url: string, data?: {}) {
        let headers = this.setHeader();
        let _data = JSON.stringify(data);
        let url = HttpService.API_BASE_URL + api_url;
        return this._http.put(url, _data, {headers: headers});
    }

    public delete(api_url: string) {
        let headers = this.setHeader();
        let url = HttpService.API_BASE_URL + api_url;
        return this._http.delete(url, {headers: headers});
    }

    private setHeader(type: string = 'application/json') {
        let headers = new HttpHeaders();

        if (type == 'application/json') {
            headers = headers.set('Accept', 'application/json');
            headers = headers.set('Content-Type', 'application/json');
        }

        if(Config.accessToken){
            headers = headers.set('Authorization', 'Bearer ' + Config.accessToken)
        }

        headers = headers.set('Accept-Language', 'pt-br');

        return headers;
    }
}
