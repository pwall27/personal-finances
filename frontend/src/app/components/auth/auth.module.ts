import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {LoginComponent} from "./login/login.component";
import {AuthRoutingModule} from './auth-routing.module';
import {FormsModule} from "@angular/forms";
import { LogoutComponent } from './logout/logout.component';

@NgModule({
  imports: [
    CommonModule,
    AuthRoutingModule,
    FormsModule
  ],
  declarations: [
    LoginComponent,
    LogoutComponent
  ]
})
export class AuthModule {
}
