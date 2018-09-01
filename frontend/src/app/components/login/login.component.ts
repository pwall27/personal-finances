import {Component} from '@angular/core';
import {User} from "../../models/user.model";
import {Router} from "@angular/router";
import {UserService} from "../../services/user.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  user: User;
  processing = false;

  constructor(private router: Router, private userService: UserService) {
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
    this.userService.login(this.user)
      .subscribe(
        (result: any) => {
          this.processing = false;
          this.router.navigate(["/list"]);
        },
        (error) => {
          this.processing = false;
          alert("Unfortunately we could not find your account.");
          console.log(error);
        });
  }
}
