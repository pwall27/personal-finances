import { Component, OnInit } from '@angular/core';
import {AuthService} from "../../../services/auth.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-logout',
  template: '',
})
export class LogoutComponent implements OnInit {

  constructor(private authService: AuthService, private router: Router) { }

  ngOnInit() {
    this.authService.logout();
    this.router.navigate(['/auth/login']);
  }

}
