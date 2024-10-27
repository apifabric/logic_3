import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CustomerSupportHomeComponent } from './home/CustomerSupport-home.component';
import { CustomerSupportNewComponent } from './new/CustomerSupport-new.component';
import { CustomerSupportDetailComponent } from './detail/CustomerSupport-detail.component';

const routes: Routes = [
  {path: '', component: CustomerSupportHomeComponent},
  { path: 'new', component: CustomerSupportNewComponent },
  { path: ':id', component: CustomerSupportDetailComponent,
    data: {
      oPermission: {
        permissionId: 'CustomerSupport-detail-permissions'
      }
    }
  }
];

export const CUSTOMERSUPPORT_MODULE_DECLARATIONS = [
    CustomerSupportHomeComponent,
    CustomerSupportNewComponent,
    CustomerSupportDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CustomerSupportRoutingModule { }