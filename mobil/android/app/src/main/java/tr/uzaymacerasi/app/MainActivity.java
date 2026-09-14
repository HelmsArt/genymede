package tr.uzaymacerasi.app;

import android.os.Bundle;
import android.view.View;
import android.view.Window;
import androidx.core.view.WindowCompat;
import androidx.core.view.WindowInsetsCompat;
import androidx.core.view.WindowInsetsControllerCompat;
import com.getcapacitor.BridgeActivity;

/* Tam ekran (sürükleyip geçici gösterilen çubuklar): çocuk uygulaması,
   durum ve gezinme çubuğu simülasyonun üstüne binmesin. */
public class MainActivity extends BridgeActivity {
  @Override
  public void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    tamEkran();
  }

  @Override
  public void onWindowFocusChanged(boolean hasFocus) {
    super.onWindowFocusChanged(hasFocus);
    if (hasFocus) tamEkran();
  }

  private void tamEkran() {
    Window w = getWindow();
    WindowCompat.setDecorFitsSystemWindows(w, false);
    View kok = w.getDecorView();
    WindowInsetsControllerCompat c = new WindowInsetsControllerCompat(w, kok);
    c.hide(WindowInsetsCompat.Type.systemBars());
    c.setSystemBarsBehavior(WindowInsetsControllerCompat.BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE);
  }
}
