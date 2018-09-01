export class Config {
    // TODO: Set apiUrl based on environment
    static apiUrl = "http://localhost:8000/api/v1";
    private _accessToken: string;

    static get accessToken(): string {
        return localStorage.getItem('accessToken');
    }

    static set accessToken(newAccessToken: string) {
        localStorage.setItem('accessToken', newAccessToken);
    }
}
