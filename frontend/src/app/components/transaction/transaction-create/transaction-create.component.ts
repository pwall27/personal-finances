import { Component, OnInit } from '@angular/core';
import {Transaction} from "../../../models/transaction.model";
import {TransactionService} from "../../../services/transaction.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-transaction-create',
  templateUrl: './transaction-create.component.html',
  styleUrls: ['./transaction-create.component.css']
})
export class TransactionCreateComponent implements OnInit {
  transaction: Transaction;
  processing: boolean = false;

  constructor(private transactionService: TransactionService, private router: Router) {
    this.transaction = new Transaction();
    this.transaction.transaction_type = 'expense';
  }

  submit() {
    if (!this.transaction.transaction_type || !this.transaction.description || !this.transaction.amount) {
      alert("Please fill out all the fields.");
      return;
    }

    this.processing = true;

    this.create();
  }

  create() {
    this.transactionService.create(this.transaction)
      .subscribe(
        (result: any) => {
          this.processing = false;
          this.router.navigate(["/transactions"]);
        },
        (error) => {
          this.processing = false;
          alert("Unfortunately something didn't workout properly, please try again.");
          console.log(error);
        });
  }

  ngOnInit() {
  }

}
