import {NgModule} from '@angular/core';
import {RouterModule, Routes} from "@angular/router";
import {TransactionListComponent} from "./transaction-list/transaction-list.component";
import {TransactionCreateComponent} from "./transaction-create/transaction-create.component";


const routes: Routes = [
  {path: "", component: TransactionListComponent},
  {path: "create", component: TransactionCreateComponent},
];

@NgModule({
  imports: [RouterModule.forChild(routes),],
  exports: [RouterModule],
  declarations: []
})
export class TransactionRoutingModule {
}
