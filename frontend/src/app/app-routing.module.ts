import {NgModule} from '@angular/core';
import {RouterModule, Routes} from "@angular/router";


const routes: Routes = [
  {path: "", redirectTo: "/transactions", pathMatch: "full"},
  {path: "auth", loadChildren: "./components/auth/auth.module#AuthModule"},
  {path: "transactions", loadChildren: "./components/transaction/transaction.module#TransactionModule"},
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule],
  declarations: []
})
export class AppRoutingModule {
}
