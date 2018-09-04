import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {TransactionRoutingModule} from './transaction-routing.module';
import {FormsModule} from "@angular/forms";
import {TransactionListComponent} from "./transaction-list/transaction-list.component";
import { TransactionCreateComponent } from './transaction-create/transaction-create.component';

@NgModule({
  imports: [
    CommonModule,
    TransactionRoutingModule,
    FormsModule
  ],
  declarations: [
    TransactionListComponent,
    TransactionCreateComponent
  ]
})
export class TransactionModule {
}
