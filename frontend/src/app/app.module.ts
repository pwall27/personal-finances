import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {FormsModule} from '@angular/forms';
import {AppComponent} from './app.component';
import {AppRoutingModule} from './app-routing.module';
import {HttpService} from "./services/http.service";
import {HttpClientModule} from "@angular/common/http";
import {UiModule} from './ui/ui.module';
import {AuthGuardService} from "./services/auth-guard.service";

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    UiModule,
  ],
  providers: [HttpService, AuthGuardService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
