import {Component} from '@angular/core';
import {Router} from "@angular/router";
import {User} from "../../../models/user.model";
import {AuthService} from "../../../services/auth.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  user: User;
  processing = false;

  constructor(private router: Router, private authService: AuthService) {
    this.user = new User();
  }

  submit() {
    if (!this.user.email || !this.user.password) {
      alert("Please provide both an email address and password.");
      return;
    }

    this.processing = true;

    this.login();
  }

  login() {
    this.authService.login(this.user)
      .subscribe(
        (result: any) => {
          this.processing = false;
          this.router.navigate(["/transactions"]);
        },
        (error) => {
          this.processing = false;
          alert("Unfortunately we could not find your account.");
          console.log(error);
        });
  }
}
