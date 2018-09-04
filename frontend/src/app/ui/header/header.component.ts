import { Component, OnInit } from '@angular/core';
import {AuthService} from "../../services/auth.service";
import {BehaviorSubject} from "rxjs/index";

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  private loggedIn = new BehaviorSubject<boolean>(false);

  constructor(private authService: AuthService) {
    this.isLoggedIn();
  }

  isLoggedIn() {
    if (this.authService.isAuthenticated()) {
      this.loggedIn.next(true);
    } else {
      this.loggedIn.next(false);
    }
    return this.loggedIn.asObservable();
  }

  ngOnInit() {
  }

}
