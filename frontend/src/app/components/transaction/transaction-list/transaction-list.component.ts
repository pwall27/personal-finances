import { Component, OnInit } from '@angular/core';
import {TransactionService} from "../../../services/transaction.service";
import {Transaction} from "../../../models/transaction.model";

@Component({
  selector: 'app-transaction-list',
  templateUrl: './transaction-list.component.html',
  styleUrls: ['./transaction-list.component.css']
})
export class TransactionListComponent implements OnInit {

  transactions: Transaction[];
  ordering = '';

  constructor(private transactionService: TransactionService) {
    this.listTransactions();
  }

  public toggleOrdering(field: string){
    if(this.ordering == field) {
      this.ordering = '-' + field;
    } else {
      this.ordering = field;
    }
    this.listTransactions();
  }

  private listTransactions(){
    this.transactionService.list(this.ordering)
      .subscribe(
        (transactions: Transaction[]) => {
          this.transactions = [];
          for (let transaction of transactions) {
            this.transactions.push(transaction);
          }
          console.log('list updated');
        },
        error => {
          console.log(error);
        }
      );
  }

  ngOnInit() {

  }

}
