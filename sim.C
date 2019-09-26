
{
  double knob = 0.5;
  
  fMain = new TGMainFrame(gClient->GetRoot(),200,200);
  fEcanvas = new TRootEmbeddedCanvas("Ecanvas",fMain,200,200);
  fMain->AddFrame(fEcanvas,new TGLayoutHints(kLHintsExpandX |
                kLHintsExpandY, 10, 10, 10, 1));

  slider = new TGHSlider(fMain, 100, kSlider1 | kScaleBoth, 111);
  slider->SetRange(0,100);
  slider->SetPosition(50);
  
  //Displaying the frame
  fMain->MapSubwindows();
  fMain->Resize(fMain->GetDefaultSize());
  fMain->MapWindow();
  
}


void DrawPlot() {
  TF1 *f1 = new TF1("f1", "sin(x)",0,gRandom->Rndm()*10);
  f1->Draw();
  TCanvas *fCanvas = fEcanvas->GetCanvas();
  fCanvas->Update();
}
