import {NgModule} from '@angular/core';
import {RouterModule, Routes} from "@angular/router";
import {TransactionListComponent} from "./transaction-list/transaction-list.component";
import {TransactionCreateComponent} from "./transaction-create/transaction-create.component";
import {AuthGuardService as AuthGuard} from "../../services/auth-guard.service";

const routes: Routes = [
  {path: "", component: TransactionListComponent, canActivate: [AuthGuard] },
  {path: "create", component: TransactionCreateComponent, canActivate: [AuthGuard] },
];

@NgModule({
  imports: [RouterModule.forChild(routes),],
  exports: [RouterModule],
  declarations: []
})
export class TransactionRoutingModule {
}
