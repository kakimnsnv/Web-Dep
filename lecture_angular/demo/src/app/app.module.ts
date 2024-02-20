import { BrowserModule } from "@angular/platform-browser";
import { AppComponent } from "./app.component";
import { NgModule } from "@angular/core";

@NgModule({
    imports: [
        BrowserModule,
        ReactiveFormsModule,
        RouterModule.forRoot([{
            path: '', component: ProductListComponent
        },])
    ],
    declarations: [
        AppComponent,
        TopBarComponent,
        ProductListComponent,
    ],
    bootstrap: [
        AppComponent
    ]
})
export class AppModule { }